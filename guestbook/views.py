from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def handle_upload(image_file):
    pass
def index(request):
    return render(request, 'guestbook/index.html')

def login(request):
    return render(request, 'guestbook/login.html')

def upload(request):
    return render(request, 'guestbook/upload.html')

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

def img_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = UploadImageForm()
    return render(request, 'guestbook/upload_image.html', {'form': form} )
