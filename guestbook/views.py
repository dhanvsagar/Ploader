from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadImage
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

# def upload_image(request):
#     if request.method == 'POST':
#         form = UploadImage(request.POST, request.files)
#         if form.is_valid():
#             handle_upload(request.FILES['file'])
#             return HttpResponseRedirect('/success/url')
#         else:
#             form = UploadImage()
#         return render(request, 'upload.html', {form: form})

def img_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'guestbook/upload_image.html', {'uploaded_file_url' : uploaded_file_url})
    return render(request, 'guestbook/upload_image.html')