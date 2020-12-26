from django.urls import path
from ..views.views_account import *

urlpatterns = [
    # ユーザー登録
    path('signup/', temp_signupfunc, name='signup'),
    # ログイン
    path('login/', loginfunc, name='login'),
    # パスワード変更
    path('change_password/', change_passfunc, name='change_pass'),
    # 利用規約
    path('terms/', termsfunc, name='terms'),
    # メール認証
    path('verify_email/<uuid:uuid>/', verifyfunc, name='verify_email'),
]
