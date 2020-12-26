from django.urls import include, path

urlpatterns = [
    # アカウント操作系
    path('account/', include('basket.urls.urls_account')),
    # 在庫管理系
    path('stock/', include('basket.urls.urls_stock')),
]
