from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"name": "name", "placeholder": "name"},
            ),
            "email": forms.EmailInput(
                attrs={"name": "email", "placeholder": "YOUR EMAIL"},
            ),
            "subject": forms.TextInput(
                attrs={"name": "subject", "placeholder": "YOUR SUBJECT"},
            ),
            "message": forms.Textarea(
                attrs={"name": "message", "placeholder": "YOUR MESSAGE"},
            ),
        }
