from django import forms
from .models import CourseContent

class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = ['title', 'file']
        # Add any other fields you need for the form