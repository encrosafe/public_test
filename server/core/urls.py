from server.core import views


urlpatterns = [
    path('', views.start_view, name='start_view'),
]