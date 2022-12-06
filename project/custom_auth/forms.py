from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "avatar", "bio", "password1", "password2", "is_artist")
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'E-Mail'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'Last Name'}),
            'Avatar': forms.FileInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'Upload Avatar'}),
            'bio': forms.TextInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'Bio'}),
            'is_artist': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control w-full rounded-sm', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control w-full rounded-sm', 'placeholder': 'Confirm Password'})
        self.fields['is_artist'].label = "I'm an artist"


class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
