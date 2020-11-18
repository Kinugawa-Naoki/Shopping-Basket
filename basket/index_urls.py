from django.urls import include, path

urlpatterns = [
    # アカウント操作系
    path('account/', include('basket.urls.account_urls'))
]
