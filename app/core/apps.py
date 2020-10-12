from django.apps import AppConfig
from .models import User


def set_user_session(request, povis_id):
    request.session['id'] = povis_id


def get_user_model(povis_id: str):
    user = User.objects.filter(povis_id=povis_id)

    if user.count() == 0:
        user = User.create(povis_id)
        user.save()
        return user

    return user[0]


def login(request, povis_id):
    user = get_user_model(povis_id)
    set_user_session(request, povis_id)
    return user


def logout(request):
    set_user_session(request, None)


def is_login(request):
    return False if request.session.get('id', None) is None else True


class CoreConfig(AppConfig):
    name = 'core'
