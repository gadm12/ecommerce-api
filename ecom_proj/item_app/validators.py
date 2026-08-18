from django.core.exceptions import ValidationError
import re


def name_format_validate(value: str):

    good_input = re.fullmatch(r"[A-Za-z0-9 :\-]+", value)

    if not good_input:
        raise ValidationError("wrong format")


def title_format_validate(value: str):

    if not value.istitle():
        raise ValidationError("wrong format")
