from django import forms
from .models import list_students,image_students


class listForm(forms.ModelForm):
   

    
    class Meta:
        model= list_students
        fields= '__all__'
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate':forms.DateInput(attrs={'class': 'form-control'}),
            
            'placeofbirth':forms.TextInput(attrs={'class': 'form-control'}),
            'class_attend':forms.TextInput(attrs={'class': 'form-control'}),
            'school':forms.TextInput(attrs={'class': 'form-control'}),
            'father':forms.TextInput(attrs={'class': 'form-control'}),
            'mother':forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model= image_students
        fields= '__all__'
    
        