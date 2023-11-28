from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    user_ip = request.META['REMOTE_ADDR']

    text = f'<h1>Host: {host}, <br>browser: {user_agent}, <br>IP: {user_ip}</h1>'
    return HttpResponse(text, headers={'SecretCode': '1225488'})


def user(request, name='noname', age=0):
    return HttpResponse(f'<h1>User {name}<br>Age: {age}</h1>')
