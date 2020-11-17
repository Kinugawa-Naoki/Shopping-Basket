from basket.views import check_emailfunc
from django.urls import include, path

urlpatterns = [
    path('account/', include('basket.account.urls'), name='account'),
    path('check_email/',check_emailfunc, name='check_email')
]
