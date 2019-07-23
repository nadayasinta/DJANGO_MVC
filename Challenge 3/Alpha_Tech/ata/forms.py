from django import forms
from .models import Mentor, Mentee, Blog

class Input_Mentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('id', 'name', 'position','experience','comment','photo')

class Input_Mentee(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('id', 'name', 'comment','photo')

class Input_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'date_create','photo')
