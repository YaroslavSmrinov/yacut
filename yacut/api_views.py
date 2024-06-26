import re
from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.constants import (EMPTY_REQUEST, FLASH_SHORT_EXISTS, LINK_MISSING,
                             LINK_NOT_FOUND_MESSAGE, LINK_REGEXP,
                             SHORT_LINK_REGEXP, WRONG_SHORT_LINK)
from yacut.errors import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_api():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(EMPTY_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(LINK_MISSING)
    if not re.match(LINK_REGEXP, data['url']):
        raise InvalidAPIUsage(WRONG_SHORT_LINK)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(FLASH_SHORT_EXISTS.format(data['custom_id']))
    if not re.match(SHORT_LINK_REGEXP, data['custom_id']):
        raise InvalidAPIUsage(WRONG_SHORT_LINK)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def redirect_api(short):
    redirect = URLMap.query.filter_by(short=short).first()
    if not redirect:
        raise InvalidAPIUsage(LINK_NOT_FOUND_MESSAGE, HTTPStatus.NOT_FOUND)
    return jsonify({'url': redirect.original})
