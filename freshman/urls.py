from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sales.views import IndexView
from freshman.auth.views import LoginView,LogoutView


urlpatterns = [
    #path('', admin.site.urls),
    path('admin/', admin.site.urls), 
    path('',IndexView.as_view()),   
    path('homepage/',include('sales.urls',namespace="homepage")),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
