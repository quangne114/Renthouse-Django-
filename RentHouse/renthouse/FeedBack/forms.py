from django import forms
from .models import FeedBack

class FeedBackCreateForm(forms.ModelForm): 
    class Meta:
        model = FeedBack
        fields = '__all__'
