from django import forms


class ProfileUpdate(forms.Form):
    name = forms.CharField(label='User name', max_length=100)
    trainername = forms.CharField(label='Trainer Name', max_length=100)


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
