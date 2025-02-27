from django import forms
from .models import TrackedActivitie

class TrackedActivitieForm(forms.ModelForm):
    # activityType = forms.TextInput()
    # duration = forms.IntegerField()
    # notes = forms.TextInput()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = TrackedActivitie
        fields = ['activityType', 'duration', 'notes', 'date']

