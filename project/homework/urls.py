from django.urls import path, re_path
from .views import info, user, error

urlpatterns = [
    path('', info, name='info'),
    re_path(r'^user/(?P<login>\D+)/(?P<directory>\D+)/(?P<post>\d+)', user),
    re_path(r'^user/(?P<login>\D+)/(?P<directory>\D+)', user),
    re_path(r'^user/(?P<login>\D+)', user),
    re_path(r'^user/', user),
    re_path(r'^', error, name='error'),

]