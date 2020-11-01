from django import forms
from .models import Item
class ItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.FileField()
    class Meta:
        model = Item
        fields = ['title', 'description', 'image']