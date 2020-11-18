from django.urls import path
from ..views import account

urlpatterns = [
    # アカウント操作系
    path('signup/', account.temp_signupfunc, name='signup'),
    path('login/', account.loginfunc, name='login'),
    path('terms/', account.termsfunc, name='terms'),
    path('verify_email/<uuid:uuid>/', account.verifyfunc, name='verify_email'),
]
