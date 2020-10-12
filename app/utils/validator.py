from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from core.models import User

import requests


def probability_limitation(target):
    if not 0 <= target <= 1:
        raise ValidationError(
            gettext("Probability must be a value between 0 and 1")
        )


def unique_id(target):
    if User.objects.filter(povis_id=target).count() > 0 :
        raise ValidationError(
            gettext("ID is Unique!")
        )


def povis_id(id):
    check_url = "https://hemos.postech.ac.kr/wp-login.php"
    res = requests.post(check_url, data={
        'log': id,
        'pwd': 'a',
        'wp-submit': 'Log In'
    })

    if "There's no such user in LDAP" in res.text:
        raise ValidationError(
            gettext("존재하지 않는 POVIS ID입니다.")
        )