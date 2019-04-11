from django import forms 



class RegistrationForm(forms.Form):
	username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
	password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
	email = forms.CharField(max_length=20, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}))
	phone = forms.CharField(max_length=20, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'phone'}))


class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)