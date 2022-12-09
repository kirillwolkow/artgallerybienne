from django import forms

from gallery.models import Post, Comment


class ArtCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "art_type",
            "file",
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'title*'}),
            'description': forms.Textarea(attrs={'class': 'w-full rounded-sm', 'placeholder': 'description (max. 300 words)*'}),
            'art_type': forms.Select(attrs={'class': 'w-full rounded-sm', 'placeholder': 'select art form*'}),
            'file': forms.FileInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'upload a file*'}),
        }


class ArtCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
        ]

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'w-full rounded-sm', 'placeholder': 'Comment'}),
        }
