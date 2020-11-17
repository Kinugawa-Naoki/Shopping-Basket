from django import forms
from django.forms.widgets import PasswordInput, Select

# ユーザー登録用フォーム
class SignupForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary text-center', 'name':'user_id'}),
        label='ユーザーID'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control text-secondary text-center', 'name':'email'}),
        label='メールアドレス'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary text-center', 'name':'user_pass'}),
        label='パスワード'
    )
    agree_terms = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class':'', 'name':'terms'}),
        label='利用規約に同意する',
        required=True,
    )

# ログイン用フォーム
class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary', 'name':'user_id'}),
        label='ユーザーID'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'user_pass'}),
        label='パスワード'
    )
