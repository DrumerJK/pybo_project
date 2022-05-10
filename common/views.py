import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from common.forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자인증
            login(request, user) # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def signup_check(request):
    result = {
        'result': 'exist'
    }
    if request.method == "POST":
        username = json.loads(request.body)
        try:
            temp = User.objects.get(username=username)
        except Exception as e:
            temp = None
        if temp is None:
            result = {
                'result': 'not exist'
            }
    return JsonResponse(result)





