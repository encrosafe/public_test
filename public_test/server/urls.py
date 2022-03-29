from django.urls import path, include

from server import views


urlpatterns = [
    path('start/', views.start_view, name='start_view'),
    path('login/success/', views.hook_after_login),
    path('', views.check_login_and_redirect),
    path('registration/', views.registration, name='registration'),
]