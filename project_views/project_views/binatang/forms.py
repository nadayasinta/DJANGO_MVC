from django import forms
from .models import Hewan

class inputbinatang(forms.ModelForm):
    class Meta:
        model = Hewan
        fields =('nama','species','berat','umur')