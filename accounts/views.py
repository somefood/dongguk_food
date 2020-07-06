from django.shortcuts import render, redirect, get_object_or_404
# from .forms import SigninForm, SignupForm, ProfileForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

import json
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm

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
        u = User.objects.get(username=self.request.user)
        context['mylists'] = u.userboard_set.all()
        return context

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):  # 역시 GET/POST 방식을 사용하여 구현한다.
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "GET":
        return render(request, 'accounts/signup.html', {'f': SignupForm(),
                                                             'ef': ProfileForm(),
                                                             })
    elif request.method == "POST":
        form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
            # cleaned_data는 사용자가 입력한 데이터를 뜻한다.
            # 즉 사용자가 입력한 password와 password_check가 맞는지 확인하기위해 작성해주었다.
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                # User.object.create_user는 사용자가 입력한 name, email, password를 가지고 아이디를 만든다.
                # 바로 .save를 안해주는 이유는 User.object.create를 먼저 해주어야 비밀번호가 암호화되어 저장된다.
                # new_user.last_name = form.cleaned_data['last_name']
                # new_user.first_name = form.cleaned_data['first_name']
                # 나머지 입력하지 못한 last_name과, first_name은 따로 지정해준다.
                # new_user.save(commit=False)
                new_user.profile.nickname = profile_form.cleaned_data['nickname']
                new_user.profile.phone_number = profile_form.cleaned_data['phone_number']
                new_user.save()
                # return render(request, 'accounts/signup_done.html', {'user_name':profile_form.cleaned_data['nickname']})
                return redirect('home')
                # return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'accounts/signup.html', {'f': form,
                                                                'ef': profile_form,
                                                                'error': '비밀번호와 비밀번호 확인이 다릅니다.'})  # password와 password_check가 다를 것을 대비하여 error를 지정해준다.
        else:  # form.is_valid()가 아닐 경우, 즉 유효한 값이 들어오지 않았을 경우는
            return render(request, 'accounts/signup.html', {'f': form,
                                                            'ef': profile_form,
                                                            })
            # return render(request, 'accounts/signup.html', {'f': form})
            # 원래는 error 메시지를 지정해줘야 하지만 따로 지정해주지 않는다.
            # 그 이유는 User 모델 클래스에서 자동으로 error 메시지를 넘겨줌
