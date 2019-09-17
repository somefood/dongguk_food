from django.shortcuts import render
from .forms import SigninForm, SignupForm, ProfileForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .models import Profile
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
# login과 authenticate 기능을 사용하기 위해 선언
# login은 로그인을 처리해주며, authenticate는 아이디와 비밀번호가 모두 일치하는 User 객체를 추출

from django.contrib.auth import logout # 로그아웃 처리하기 위해 선언

from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def signin(request): #로그인 기능
    if request.method == "GET":
        return render(request, 'accounts/signin.html', {'f':SigninForm})
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
	    # authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
	    # 만약 같으면 해당 객체를 반화하고 아니라면 none을 반환한다.

        if u: # u에 특정 값이 있다면,
            login(request, user=u) # u 객체로 로그인해라
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'accounts/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):  # 역시 GET/POST 방식을 사용하여 구현한다.
    if request.method == "GET":
        if not request.GET.get('type', None):
            return render(request, 'accounts/sign_term00.html')
        return render(request, 'accounts/sign_term01.html', {'type': request.GET['type'],
                                                             'f': SignupForm(),
                                                             'ef': ProfileForm(),
                                                             })
        # return render(request, 'accounts/signup.html', {'f': SignupForm(),
        #                                                 'ef': ProfileForm()
        #                                                 })
        # return render(request, 'accounts/signup.html', {'f': SignupForm()})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
            # cleaned_data는 사용자가 입력한 데이터를 뜻한다.
            # 즉 사용자가 입력한 password와 password_check가 맞는지 확인하기위해 작성해주었다.
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],form.cleaned_data['password'])
                # User.object.create_user는 사용자가 입력한 name, email, password를 가지고 아이디를 만든다.
                # 바로 .save를 안해주는 이유는 User.object.create를 먼저 해주어야 비밀번호가 암호화되어 저장된다.
                # new_user.last_name = form.cleaned_data['last_name']
                # new_user.first_name = form.cleaned_data['first_name']
                # 나머지 입력하지 못한 last_name과, first_name은 따로 지정해준다.
                # new_user.save(commit=False)
                new_user.profile.nickname = profile_form.cleaned_data['nickname']
                new_user.profile.phone_number = profile_form.cleaned_data['phone_number']
                new_user.profile.address = profile_form.cleaned_data['address']
                new_user.profile.faFT = profile_form.cleaned_data['faFT']
                new_user.profile.agree = request.POST['type']
                new_user.save()
                return render(request, 'accounts/sign_finish.html', {'user_name':profile_form.cleaned_data['nickname']})
                # return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'accounts/sign_term01.html', {'f': form,
                                                                'ef': profile_form,
                                                                'error': '비밀번호와 비밀번호 확인이 다릅니다.'})  # password와 password_check가 다를 것을 대비하여 error를 지정해준다.
        else:  # form.is_valid()가 아닐 경우, 즉 유효한 값이 들어오지 않았을 경우는
            return render(request, 'accounts/sign_term01.html', {'f': form,
                                                            'ef': profile_form,
                                                            })
            # return render(request, 'accounts/signup.html', {'f': form})
            # 원래는 error 메시지를 지정해줘야 하지만 따로 지정해주지 않는다.
            # 그 이유는 User 모델 클래스에서 자동으로 error 메시지를 넘겨줌
