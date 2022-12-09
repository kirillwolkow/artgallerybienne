from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

User = settings.AUTH_USER_MODEL

PAINTING = "PAI"
DRAWING = "DRA"
SCULPTURE = "SCU"
ARCHITECTURE = "ARC"
LITERATURE = "LIT"
MUSIC = "MUS"
THEATER = "THE"
DANCE = "DAN"
CINEMA = "CIN"
PHOTOGRAPHY = "PHO"

TYPE_CHOICES = [
        (PAINTING, _('Painting')),
        (DRAWING, _('Drawing')),
        (SCULPTURE, _('Sculpture')),
        (ARCHITECTURE, _('Architecture')),
        (LITERATURE, _('Literature')),
        (MUSIC, _('Music')),
        (THEATER, _('Theater')),
        (DANCE, _('Dance')),
        (CINEMA, _('Cinema')),
        (PHOTOGRAPHY, _('Photography')),
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
    art_type = models.CharField(
        _('art type'),
        max_length=150,
        choices=TYPE_CHOICES,
        default=PAINTING,
        help_text="Choose your type of art.",
        blank=True,
        )
    file = models.FileField(
        _('file'),
        upload_to='artworks/%Y/%m/%d/',
        blank=True, null=True
    )
    is_stage = models.BooleanField(default=True)
    is_showroom = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='art_posts', blank=True, null=True)

    def total_likes(self):
        return self.likes.count()

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
        on_delete=models.CASCADE,
        related_name='comments',
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
        return '%s - %s' % (self.post.title, self.comment)
