import json

from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import UserModel


@ensure_csrf_cookie
def outside(request):
    if request.method == "POST":
        if request.POST.get('username')==None:
            return HttpResponse('Error. Input name.')
        else:
            return index(add_user(request.POST['username']))
    else:
        if request.GET.get('username')==None:
            return index()
        else:
            return index(request.GET['username'])

def index(filter=None):
    users_list = []
    if filter!=None:
        users_list = [ob.to_dict() for ob in UserModel.objects.filter(username=filter)]
    else:
        users_list = [ob.to_dict() for ob in UserModel.objects.all()]
    context_dict = json.dumps(users_list)

    return HttpResponse(context_dict)

def add_user(username):
    return UserModel.objects.get_or_create(username=username)[0]
