
from django import forms
from uploadapp.models import UploadFile, UploadImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'

# form model for upload file table or model
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'