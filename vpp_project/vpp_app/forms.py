from django import forms
from .models import ContactLead

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactLead
        fields = '__all__'