from django.shortcuts import render, redirect
from django.views import View
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .apps import login, is_login, logout

from roulette.models import Item

from utils.validator import povis_id


class LoginForm(forms.Form):
    id = forms.CharField(max_length=50, validators=[povis_id])


class LoginView(View):
    def get(self, request):
        if is_login(request):
            return redirect('/')
        form = LoginForm()
        return render(request, 'core/login.html', {
            'form': form
        })

    def post(self, request):
        if is_login(request):
            return redirect('/')
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'core/login.html', {
                'form': form
            })

        login(request, form.cleaned_data['id'])
        return redirect('roulette')


class LogoutView(View):
    def get(self, request):
        if is_login(request):
            logout(request)

        return redirect('/')


class HomeView(View):
    def get(self, request):
        items = Item.objects.all()

        return render(request, 'core/index.html', {
            'test': request.session.get('id', 'nothing!'),
            'items': items,
            'povis_id': request.session.get('id', None)
        })
