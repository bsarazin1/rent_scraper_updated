from django.urls import path
from django.conf.urls import static, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.search, name='index'),
    path('user/', include('accounts.urls')),
    path('<int:id>/userpage', views.user_page, name='userpage'),
    path("", views.delete, name="delete"),
]
