from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "Все"),
        ("todo", "To Do"),
        ("in_progress", "In progress"),
        ("done", "Done"),
    ]
    
    PRIORITY_CHOICES = [
        ("", "Все"),
        ("low", "Low"),
        ("mid", "Medium"),
        ("high", "High")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False, label="Приоритет")
