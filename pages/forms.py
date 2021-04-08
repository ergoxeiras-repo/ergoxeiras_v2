from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Όνομα', widget=forms.TextInput(attrs={
        'class': 'form-control'
        }))
    subject = forms.CharField(label='Θέμα', widget=forms.TextInput(attrs={
        'class': 'form-control'
        }))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'class': 'form-control'
        }))
    body = forms.CharField(label='Γράψτε το μήνυμά σας', widget=forms.Textarea(
        attrs={'class': 'form-control'}
    ))
