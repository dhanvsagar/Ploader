import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Image
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            redirect('')
    else:
        form = AuthenticationForm
        return render(request,'guestbook/login.html', {'form': form})

def handle_upload(image_file):
    pass

# def login(request):
#     return render(request, 'guestbook/login.html')

def about(request):
    return render(request, 'guestbook/about.html')

# def img_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'guestbook/upload_image.html', {'uploaded_file_url' : uploaded_file_url})
#     return render(request, 'guestbook/upload_image.html')

def upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadImageForm()
    return render(request, 'guestbook/upload_image.html', {'form': form} )

def index(request):
    img_list = Image.objects.all()
    img_names = {'img_list':  img_list}
    return render(request, 'guestbook/index.html', img_names)