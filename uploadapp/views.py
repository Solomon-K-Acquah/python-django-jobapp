from django.http import HttpResponse
from django.shortcuts import render

from uploadapp.forms import UploadFileForm, UploadForm

# Create your views here.
def upload_image(request):

    if request.method == "POST": 
        # creating instance of upload form model
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()

            # get the instance of form items
            saved_object = form.instance

            return render(request, 'uploadapp/add_image.html', {'form':form, 'saved_object': saved_object})
    else:
        form = UploadForm()

    return render(request, 'uploadapp/add_image.html', {'form': form})

# upload file function
def upload_file(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # getting the saved data instance
            saved_data = form.instance
            return render(request, 'uploadapp/add_file.html', {'form':form, 'saved_data':saved_data})
    else:
        form = UploadFileForm()

    return render(request, 'uploadapp/add_file.html', {'form':form})
