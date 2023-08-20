from django import forms


from .models import Store

CLASS_INPUT = 'form-control w-full rounded-xl border mb-4 mt-2'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'manager', 'address']

        widgets = {
            'name': forms.TextInput(attrs={
            'class': CLASS_INPUT
            }),
            'manager': forms.TextInput(attrs={
            'class': CLASS_INPUT
            }),

            'address': forms.Textarea(attrs={
            'class': CLASS_INPUT
            }),
        }