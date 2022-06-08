from importlib.resources import path


from django.urls import path
from .views import SaleDeleteView, SaleInputView, SaleList, SaleListView,SaleNotice,SaleInput, SaleNoticeView,SaleUpdate,SaleDelete, SaleUpdateView

app_name = "homepage"

urlpatterns = [
    path('',SaleListView.as_view(), name='List'),
    path('<int:pk>/',SaleNoticeView.as_view(), name='Notice'),
    path('<int:pk>/update',SaleUpdateView.as_view(), name='Update'),
    path('<int:pk>/delete',SaleDeleteView.as_view(), name='Delete'),
    path('input/',SaleInputView.as_view(), name='Input')
]