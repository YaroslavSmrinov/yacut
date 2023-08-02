from flask import render_template, jsonify
from http import HTTPStatus
from . import app, db
from .constants import LINK_NOT_FOUND_MESSAGE, INTERNAL_ERROR_MESSAGE


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error_message=LINK_NOT_FOUND_MESSAGE), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', error_message=INTERNAL_ERROR_MESSAGE), 500


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code
