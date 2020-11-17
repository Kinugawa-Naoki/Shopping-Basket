from .models import UserProfile
from django.shortcuts import redirect, render
from .account.views import verify_email

def check_emailfunc(request):
    model = UserProfile.objects.get(pk=request.user)
    if model.verifid_email:
        return redirect('main')
    else:
        verify_email(request.user.email)
        return render(request, 'process_completed.html', {'Message':'メールの送信が完了しました。'})