from django.urls import path, re_path
from .views import index, user

urlpatterns = [
    path('', index, name='home'),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', user),
    re_path(r'^user/(?P<name>\D+)', user),
    re_path(r'^user/', user)
    # path('user/<str:name>/<int:age>', user, name='user'),
]