from django import forms

# ユーザー登録用フォーム
class SignupForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary text-center', 'name':'user_id'}),
        label='ユーザーID',
        max_length=100
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control text-secondary text-center', 'name':'email'}),
        label='メールアドレス',
        max_length=100
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary text-center', 'name':'password'}),
        label='パスワード',
        max_length=100
        )
    agree_terms = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class':'', 'name':'terms'}),
        label='利用規約に同意する',
        required=True,
        )

# パスワード入力フォーム
class CreatePassForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary text-center', 'name':'password'}),
        label='パスワード',
        max_length=100
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary text-center', 'name':'password2'}),
        label='パスワード（再入力）',
        max_length=100
    )

# ログイン用フォーム
class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary', 'name':'user_id'}),
        label='ユーザーID'
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'password'}),
        label='パスワード'
        )

# パスワード変更フォーム
class ChangePassForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text-secondary', 'name':'user_id'}),
        label='ユーザーID'
        )
    old_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'old_pass'}),
        label='現在のパスワード'
        )
    new_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control text-secondary', 'name':'new_pass'}),
        label='新しいパスワード'
        )
