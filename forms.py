from . models import Contact
from django import forms
from django.contrib.auth.models import User, auth


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			 'Username','Password','UserType',
			]
		widgets = {
            'Password': forms.PasswordInput(),
        }

        
    
        
		
	
