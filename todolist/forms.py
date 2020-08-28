from django import forms
from .models import todoItem

class todoForm(forms.ModelForm):
    class Meta:
        model = todoItem
        fields = ["author","content","is_completed"]