from django import forms
from .models import Tasks

# Reordering Form and View


class TaskUpdateForm(forms.ModelForm):
    task = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "task",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )

    class Meta:
        model = Tasks
        fields = ("task",)
