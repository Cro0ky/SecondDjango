from django.http import HttpResponse
from django.shortcuts import render


def info(request):
    user_ip = request.META['REMOTE_ADDR']
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse(f'<h1>Host: {host}, <br>browser: {user_agent}, <br>IP: {user_ip}</h1>')


def user(request, login='NONE', directory='NONE', post=0):
    return HttpResponse(f'<h1>Login {login}<br>Dir: {directory}<br>post: {post}</h1>')


def error(request):
    # status = request.META['FILE_UPLOAD_PERMISSIONS']
    err = f'<h1>error: 404</h1> '

    return HttpResponse(f'<h1>Произошла ошибка <br>status: 400', status=400, reason='Not Found')
