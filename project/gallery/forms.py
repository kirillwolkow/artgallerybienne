from django import forms

from gallery.models import Post


class ArtCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
