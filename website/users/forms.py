from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model




class UserAddingForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'profile_image', 'store', 'job', 'rol']

        widgets = {
            'first_name': forms.TextInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),
            'last_name': forms.TextInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),

            'username': forms.TextInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),

            'password1': forms.PasswordInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),

            'password2': forms.PasswordInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),

            'profile_image': forms.FileInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),
            'store': forms.Select(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),
            'job': forms.TextInput(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),

            'rol': forms.Select(attrs={
            'class': 'form-control w-full rounded-xl border'
            }),
            

            
            

        }

        def save(self, commit=True):
            user = super(UserAddingForm, self).save(commit=False)
            if commit:
                user.save()

            return user
        