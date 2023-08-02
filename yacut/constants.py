from random import choices
from string import ascii_letters, digits

from yacut.models import URLMap


# General
def get_unique_short_id():
    while True:
        short_link = ''.join(choices(ascii_letters + digits, k=6))
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link


ALLOWED_SYMBOLS = ascii_letters + digits
long_strin_to_test = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
# URLForm
# Given link form field
GIVEN_LINK_LENGTH = 2000
GIVEN_LINK_MESSAGE = "Ссылка для сокращения"
ERROR_FIELD_EMPTY = "Нечего сокращать, введите ссылку."
# Users custom field
CUSTOMISED_SHORT_LINK_LENGTH = 16
CUSTOMISED_LINK_MESSAGE = "Ваш вариант (<16 [a-zA-Z0-9])."
ERROR_DISALLOWED_SYMBOL = "Введены недоспустимые символы."
# Button
SUBMISSION_BUTTON = "Сократить"

# Errors
LINK_NOT_FOUND_MESSAGE = "Указанный id не найден"
INTERNAL_ERROR_MESSAGE = "Ошибка на стороне сервера. Попробуйте позже"

# Views
FLASH_SHORT_EXISTS = "Имя \"{}\" уже занято."

# API
EMPTY_REQUEST = "Отсутствует тело запроса"
LINK_MISSING = "\"url\" является обязательным полем!"
LINK_REGEXP = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'
WRONG_SHORT_LINK = "Указано недопустимое имя для короткой ссылки"
SHORT_LINK_REGEXP = r'^[A-Za-z0-9_]{1,16}$'
