# app_name/forms.py

from django import forms
from .models import Collaborator, Department


class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['department', 'name', 'email']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']