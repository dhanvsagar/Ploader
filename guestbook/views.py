from django.shortcuts import render

def index(request):
    return render(request, 'guestbook/index.html')

def login(request):
    return render(request, 'guestbook/login.html')

def upload(request):
    return render(request, 'guestbook/upload.html')
