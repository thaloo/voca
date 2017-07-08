from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['vocabulary'].widget.attrs['placeholder'] = "WORD"
        self.fields['meaning'].widget.attrs['placeholder'] = "TRANSLATION"
        self.fields['reference'].widget.attrs['placeholder'] = "REFERENCE"

    class Meta:
        model = Post
        fields = ('vocabulary', 'meaning', 'reference')
