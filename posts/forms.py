from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'category', 'user']
        error_messages = {
            'title': {
                'required': "Please enter a title.",
                'min_length': "Title must be at least 5 characters long."
            },
            'description': {
                'required': "Please enter a description.",
                'min_length': "Description must be at least 10 characters long."
            },
            'image': {
                'required': "Please select an image."
            },
            # Add more error messages for other fields if needed
        }
