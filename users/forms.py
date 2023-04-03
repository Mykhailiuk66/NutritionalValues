from django.forms import ModelForm, CharField, EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    first_name = CharField(max_length=150, required=True)
    last_name = CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2')
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': 'John'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': 'Smith'})
        self.fields['username'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': 'john_smith'})
        self.fields['email'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': 'johnsmith@example.com'})
        self.fields['password1'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': '************'})
        self.fields['password2'].widget.attrs.update({'class': 'w-full -ml-10 pl-10 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500', 'placeholder': '************'})


