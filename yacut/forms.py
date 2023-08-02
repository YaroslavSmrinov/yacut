from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from yacut.constants import (CUSTOMISED_LINK_MESSAGE,
                             ERROR_FIELD_EMPTY,
                             GIVEN_LINK_LENGTH, GIVEN_LINK_MESSAGE,
                             SUBMISSION_BUTTON, ERROR_DISALLOWED_SYMBOL)
from yacut.validators import CUSTOMISED_LINK_VALIDATOR


class URLForm(FlaskForm):
    original_link = URLField(
        GIVEN_LINK_MESSAGE,
        validators=[
            DataRequired(message=ERROR_FIELD_EMPTY),
            Length(max=GIVEN_LINK_LENGTH),
            URL()
        ]
    )
    custom_id = StringField(
        CUSTOMISED_LINK_MESSAGE,
        validators=[
            Optional(),
            Regexp(CUSTOMISED_LINK_VALIDATOR, message=ERROR_DISALLOWED_SYMBOL),
        ]
    )  # ''.join(choices(ascii_letters + digits, k=6))

    submit = SubmitField(SUBMISSION_BUTTON)
