from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('scrapes.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),

]
