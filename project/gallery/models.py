from django.db import models
from django.utils.translation import gettext as _

from custom_auth.models import User


TYPE_CHOICES = [
        ('Painting', _('Painting')),
        ('Drawing', _('Drawing')),
        ('Sculpture', _('Sculpture')),
        ('Architecture', _('Architecture')),
        ('Literature', _('Literature')),
        ('Music', _('Music')),
        ('Theater', _('Theater')),
        ('Dance', _('Dance')),
        ('Cinema', _('Cinema')),
    ]


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        _('title'),
        max_length=150,
        unique=True,
        help_text="Choose a title for your artwork. It can't be longer than 150 characters and is unique.",
        )
    description = models.TextField(
        _('description'),
        help_text="Describe your artwork in your own words. What are your thoughts and what's the intention behind your masterpiece.",
        null=True,
        blank=True,
    )
    type = models.CharField(
        _('type'),
        max_length=150,
        choices=TYPE_CHOICES,
        help_text="Choose your type of art.",
        )
    file = models.FileField(_('file'), upload_to='artworks/')
    is_stage = models.BooleanField(default=True)
    is_showroom = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Upvote(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_artist = models.BooleanField(default=False)
    is_enthusiast = models.BooleanField(default=True)
    is_collaborator = models.BooleanField(default=False)

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_artist = models.BooleanField(default=False)
    is_enthusiast = models.BooleanField(default=True)
    is_collaborator = models.BooleanField(default=False)
    comment = models.TextField(
        _('comment'),
        help_text="Share your toughts.",
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.comment
