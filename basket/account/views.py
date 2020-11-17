from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from uuid import uuid4

# 認証メールを送信する関数
def verify_email(R, email):
    # R = request
    # 期限切れセッションを削除
    R.session.clear_expired()
    uuid = uuid4()
    # メール送信
    subject, from_email = 'メールアドレス認証', 'naoki.kinugawa@gmail.com'
    text_content = ''
    html_content = ''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    # 30分のセッション開始
    R.session['verify_email'] = str(uuid)
    R.session.set_expiry(1800)
    return True

# 仮登録
def temp_signupfunc(request):
    signup_form = SignupForm
    if request.method == 'POST':
        user_id = request.POST['user_id']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username=user_id)
            return render(request,'signup.html', {'signup_form':signup_form, 'Error':'このユーザーはすでに登録されています'})
        except:
            # ユーザー登録する
            User.objects.create_user(user_id, email, password)
            # メール送信
            verify_email(request, email)
            return render(request, 'process_completed.html', {'Message':'仮登録が完了しました'})
    else:
        return render(request, 'signup.html', {'signup_form':signup_form})

# メール認証部
def verifyfunc(request, uuid):
    try:
        session_uuid = request.session['verify_email']
        if uuid == session_uuid:
            return render(request, 'process_completed.html', {'Message':'メールアドレスの認証が完了しました'})
        else:
            return render(request, 'html', {'Error':'セッションの有効期限が切れました'})
    except:
        return render(request, 'html', {'Error':'セッションの有効期限が切れました'})

# ログイン画面
def loginfunc(request):
    login_form = LoginForm
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(username=user_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'login_form':login_form, 'Error':'ログインに失敗しました'})
    else:
        return render(request, 'login.html', {'login_form':login_form})

# パスワード変更
@login_required
def change_pass(request):
    username = request.user
    if request.method =='POST':
        # 入力情報取り出し
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        try:
            user = authenticate(request, username=username, password=old_password)
            user_info = User.objects.get(username=username)
            user_info.set_password(new_password)
        except:
            return render(request, 'change_password.html', {'Error':'パスワードが間違っています'})

# 利用規約
def termsfunc(request):
    return render(request, 'terms.html', {'terms':'terms'})

