from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name ='account'

urlpatterns =[
    path('login/',LoginView.as_view(template_name='account/login.html'),name ='login'),
    # path('login/',views.login,name ='login'),
    path('logout/',LogoutView.as_view(),name ='logout'),
    path('signup/',views.signup, name ='signup'),
    path('account_details/<int:pk>',views.account_details.as_view(), name ='account_details'),
    path('userupdate/<int:pk>',views.userupdate, name ='userupdate'),
    
]