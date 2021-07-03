from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

# UserCreationForm을 상속받은 forms.py 추가 
from account.forms import CreateUserForm

# Create your views here.

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


