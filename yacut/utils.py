from random import choices
from string import ascii_letters, digits

from yacut.constants import LENGTH_OF_GENERATED_LINK
from yacut.models import URLMap


def get_unique_short_id():
    while True:
        short_link = ''.join(choices(
            ascii_letters + digits,
            k=LENGTH_OF_GENERATED_LINK
        ))
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link
