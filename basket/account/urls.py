from django.urls import path
from .views import temp_signupfunc, loginfunc, termsfunc, verifyfunc

urlpatterns = [
    path('signup/', temp_signupfunc, name='signup'),
    path('verify_email/<uuid:uuid>/', verifyfunc, name='verify'),
    path('login/', loginfunc, name='login'),
    path('terms/', termsfunc, name='terms')
]
