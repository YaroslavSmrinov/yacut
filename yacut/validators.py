import re

from yacut.constants import ALLOWED_SYMBOLS

# URLForm user link validators
CUSTOMISED_LINK_VALIDATOR = re.compile(rf'^[{re.escape(ALLOWED_SYMBOLS)}]*$')
