from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone, dateformat
from .models import Round, Item
from .apps import get_round, random_item, get_upcoming_rounds
from core.apps import is_login, get_user_model
from utils.mail import send_roulette_result
import logging

from utils.msg import RESULT_NOTHING, CURRENT_ROUND_NONE, ALREADY_JOIND_ROUND


logger = logging.getLogger(__name__)


class RouletteView(View):
    def get(self, request):
        if not is_login(request):
            return redirect('login')

        rnd = get_round()
        user = get_user_model(request.session['id'])
        all_rnds = Round.objects.all()
        items = Item.objects.all()

        if rnd is None:
            return render(request, 'roulette/index.html', {
                'rnd': None,
                'rounds': all_rnds,
                'items': items,
                'povis_id': user.povis_id
            })

        is_valid_round = not user.is_joined_round(rnd)
        return render(request, 'roulette/index.html', {
            'rnd': rnd,
            'is_valid': is_valid_round,
            'rounds': all_rnds,
            'items': items,
            'povis_id': user.povis_id
        })

    def post(self, request):
        if not is_login(request):
            return redirect('login')

        rnd = get_round()

        user = get_user_model(request.session['id'])

        if rnd is None:
            logger.warning(f"[None] {user.povis_id} - Not Round, but Tried...")
            return render(request, 'roulette/index.html', {
                'round_name': CURRENT_ROUND_NONE,
                'povis_id': user.povis_id
            })

        if user.is_joined_round(rnd):
            logger.warning(f"[None] {user.povis_id} - Already joined, but Tried...")
            return render(request, 'roulette/result.html', {
                'result': ALREADY_JOIND_ROUND,
                'povis_id': user.povis_id
            })

        if user.povis_id != "mzg00":
            user.join_round(rnd)
        user_item = random_item()

        if user_item is None or user_item.users.filter(povis_id=user.povis_id).count() > 0:
            logger.info(f"[{rnd.name}] {user.povis_id} - Failed...")
            return render(request, 'roulette/result.html', {
                'is_roulette': True,
                'result': RESULT_NOTHING,
                'povis_id': user.povis_id
            })

        user_item.win(user)
        send_roulette_result(user.povis_id, user_item.name, user_item.num, rnd.name,
                             dateformat.format(timezone.localtime(), 'Y년 m월 d일 H:i:s'))

        logger.info(f"[{rnd.name}] {user.povis_id} - {user_item.name} - Remaining {user_item.num}")
        return render(request, 'roulette/result.html', {
            'is_roulette': True,
            'result': user_item.name,
            'povis_id': user.povis_id,
            'img_src': user_item.img
        })
