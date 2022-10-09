from django.db import models
from django.utils.translation import ugettext_lazy as _

from custom_auth.models import User


TYPE_CHOICES = [
        ('Painting', 'Painting'),
        ('Drawing', 'Drawing'),
        ('Sculpture', 'Sculpture'),
        ('Architecture', 'Architecture'),
        ('Literature', 'Literature'),
        ('Music', 'Music'),
        ('Theater', 'Theater'),
        ('Dance', 'Dance'),
        ('Cinema', 'Cinema'),
    ]


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=150, 
        unique=True,
        help_text="Choose a title for your artwork. It can't be longer than 150 characters and is unique.",
        )
    description = models.TextField(
        help_text="Describe your artwork in your own words. What are your thoughts and what's the intention behind your masterpiece.",
        null=True,
        blank=True,
    )
    type = models.CharField(
        max_length=150,
        choices=TYPE_CHOICES,
        help_text="Choose your type of art.",
        )
    file = models.FileField(upload_to='')
    is_stage = models.BooleanField(default=True)
    is_showroom = models.BooleanField(default=False)

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
        help_text="Share your toughts.",
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.comment
