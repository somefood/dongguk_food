from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

import json
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm, FindUserForm

from django.contrib.auth import logout # 로그아웃 처리하기 위해 선언


def check_user(request):
    cUser = get_user_model()
    if not cUser.objects.filter(username=request.POST.get('user_name')).exists():
        print('possible')
        context = {'msg': True}
    else:
        print('impossible')
        context = {'msg': False}
    return HttpResponse(json.dumps(context), content_type="application/json")


def check_nickname(request):
    cUser = get_user_model()
    if not cUser.objects.filter(nickname=request.GET.get('user_nickname')).exists():
        print('possible')
        context = {'msg': True}
    else:
        print('impossible')
        context = {'msg': False}
    return HttpResponse(json.dumps(context), content_type="application/json")


class FindUser(FormView):
    form_class = FindUserForm
    template_name = 'accounts/find_user.html'

    def form_valid(self, form):
        nickname = form.cleaned_data['nickname']
        phone_number = form.cleaned_data['phone_number']
        cUser = get_user_model()
        context = {}
        try:
            user = cUser.objects.get(nickname=nickname, phone_number=phone_number)
        except ObjectDoesNotExist:
            context['error'] = '일치하는 아이디가 없습니다.'
        else:
            context['username'] = user.username
        return render(self.request, 'accounts/find_user_done.html', context=context)


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/signin.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


class UserSignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:signup_done')


class UserSignUpDoneView(TemplateView):
    template_name = 'accounts/signup_done.html'


class MyPageV(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cUser = get_user_model()
        u = cUser.objects.get(username=self.request.user)
        context['mylists'] = u.userboard_set.all()
        return context


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))