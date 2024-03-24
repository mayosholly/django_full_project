# categories/forms.py

from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': "The category name field is required.",
                'max_length': "The category name cannot exceed 100 characters."
            },
            'description': {
                'max_length': "The description cannot exceed 255 characters."
            }
        }