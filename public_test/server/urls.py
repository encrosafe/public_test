from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from server import views


urlpatterns = [
    path('admin/', admin.site.urls, name='backend'),
    path('start/', views.start_view, name='start_view'),
    path('', views.check_login_and_redirect),
    path('', include('django.contrib.auth.urls')),
    path('login/success/', views.hook_after_login),
    path('hassler/', views.hassler, name='hassler'),
    path('index/', views.index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )