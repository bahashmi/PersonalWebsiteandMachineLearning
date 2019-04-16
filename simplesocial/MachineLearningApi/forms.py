from django import forms

class EventsForm(forms.Form):
    docfile = forms.FileField(
        label="Select a File",
        help_text="Max. 42 megabytes"
    )
