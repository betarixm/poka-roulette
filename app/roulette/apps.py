from django.apps import AppConfig
import random
from .models import Item, Round
from django.utils import timezone


def random_item():
    rnd = random.random()
    threshold = 0

    items = Item.objects.all()

    for item in items:
        threshold += item.probability

        if rnd < threshold and item.num > 0:
            return item

    return None


def get_round():
    rounds = Round.objects.all()
    for r in rounds:
        if r.is_valid_time(timezone.localtime()):
            return r
    return None


def get_upcoming_rounds():
    rounds = Round.objects.all()

    l = []
    for r in rounds:
        if timezone.localtime() < r.start_time:
            l.append(r)

    return l


class RouletteConfig(AppConfig):
    name = 'roulette'
