from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import SignupForm, LoginForm, ChangePassForm
from ..models import UserProfile
from uuid import uuid4
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

# 認証情報作成・認証メール送信用関数
def send_verify_email(user_id, email, password):
    try:
        # 認証情報を発行
        uuid = uuid4()
        # ユーザー情報をデータベースに保存
        model = UserProfile(user_id=user_id, email=email, password=password, uuid=uuid, timeout = datetime.now(JST))
        model.save()
        # メール送信
        subject, from_email = 'メールアドレス認証', 'naoki.kinugawa@gmail.com'
        text_content = render_to_string('account/email_template_txt.html', {'email':email, 'uuid':uuid})
        html_content = render_to_string('account/email_template.html', {'email':email, 'uuid':uuid})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return True
    except:
        return False

# 仮登録
def temp_signupfunc(request):
    signup_form = SignupForm(request.POST)
    # 前回までのセッションを削除
    if request.method == 'POST':
        if signup_form.is_valid():
            user_id = signup_form.cleaned_data.get('user_id')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')
            try:
                # 重複するuser_idが存在しないか確認する
                User.objects.get(username=user_id)
                return render(request,'account/signup.html', {'signup_form':signup_form, 'Error':'このユーザーはすでに登録されています'})
            except:
                # メールを送信する
                if send_verify_email(user_id, email, password):
                    return render(request, 'process_completed.html', {'Message':'仮登録が完了しました'})
                return render(request, 'process_completed.html', {'Error':'予期せぬエラーが発生しました。'})
        else:
            return render(request, 'account/signup.html', {'signup_form':signup_form})
    else:
        return render(request, 'account/signup.html', {'signup_form':signup_form})

# ログイン画面
def loginfunc(request):
    login_form = LoginForm(request.POST)
    if request.method == 'POST':
        if login_form.is_valid():
            user_id = login_form.cleaned_data.get('user_id')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=user_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('terms')
            else:
                return render(request, 'account/login.html', {'login_form':login_form, 'Error':'ログインに失敗しました'})
        else:
            return render(request, 'account/login.html', {'login_form':login_form})
    else:
        return render(request, 'account/login.html', {'login_form':login_form})

# パスワード変更（未完成）
@login_required
def change_passfunc(request):
    form =  ChangePassForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            # 入力情報取り出し
            user_id = form.cleaned_data.get('user_id')
            old_password = form.cleaned_data.get('old_pass')
            new_password = form.cleaned_data.get('new_pass')
            # IDとPassがあっているか確認
            user = authenticate(username=user_id, password=old_password)
            if user is not None:
                user_info = User.objects.get(username=user_id)
                user_info.set_password(new_password)
                user_info.save()
                return render(request, 'process_completed.html', {'Message':'パスワードの変更が完了しました'})
            else:
                return render(request, 'account/change_password.html', {'form':form, 'Error':'IDまたはパスワードが間違っています'})
        else:
            return render(request, 'account/change_password.html', {'form':form})
    else:
        return render(request, 'account/change_password.html', {'form':form})

# 利用規約
def termsfunc(request):
    return render(request, 'account/terms.html', {'terms':'terms'})

# メール認証部
def verifyfunc(request, uuid):
    try:
        # モデルを参照
        model = UserProfile.objects.get(uuid=uuid)
        remain_time = datetime.now(JST) - model.timeout
        onehour = timedelta(hours=1)
        # 1時間以内に認証しているか
        if remain_time <= onehour:
            User.objects.create_user(model.user_id, model.email, model.password)
            return render(request, 'process_completed.html', {'Message':'メールアドレスの認証が完了しました'})
        else:
            # 期限切れのモデルを削除
            model.delete()
            return render(request, 'process_completed.html', {'Error':'セッションの有効期限が切れました'})
    except:
        return render(request, 'process_completed.html', {'Error':'セッションの有効期限が切れました'})
