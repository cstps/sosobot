from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

# UserCreationForm을 상속받은 forms.py 추가 
from account.forms import CreateUserForm

# Create your views here.

# 로그인 
# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_login(request, form.get_user())
#             return redirect('index')
#         return redirect('account:login')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'account/login.html', {'form': form})

# 회원가입하기
def signup(request):
    # 계정 생성
    if request.method == "POST":
        print("POST")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_login(request, user)
            return redirect('index')
    else:
        form = CreateUserForm()
        return render(request, 'account/signup.html', {'form':form})

# 사용자 정보 보기
class account_details(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/account_details.html'

# 사용자 정보 수정
def userupdate(request):
    if request.method =="GET":
        return render(request, 'account/user_info_modify.html',)
    elif request.method == 'POST':
        user = request.user

        profile_msg = request.POST.get('profile_msg')
        email = request.POST.get('email')
        name = request.POST.get('name')
        new_user_pw = request.POST.get('new_user_pw')

        user.profile_msg = profile_msg
        user.email = email
        user.first_name = name
        user.set_password(new_user_pw)

        user.save()


        return redirect('instagram:list', user.username)