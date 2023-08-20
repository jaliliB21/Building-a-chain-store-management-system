from django import forms


from .models import News

CLASS_INPUT = 'form-control w-full rounded-xl border mb-4 mt-2'

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'text', 'news_image']


        widgets = {
            'title': forms.TextInput(attrs={
            'class': CLASS_INPUT
            }),

            'description': forms.TextInput(attrs={
            'class': CLASS_INPUT
            }),

            'text': forms.Textarea(attrs={
            'class': CLASS_INPUT
            }),

            'news_image': forms.FileInput(attrs={
            'class': CLASS_INPUT
            }),
        }