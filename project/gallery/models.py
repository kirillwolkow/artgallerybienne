from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=150, 
        unique=True,
        help_text="Choose a title for your artwork. It can't be longer than 150 characters and is unique.",
        )
    type = models.CharField(
        max_length=150,
        choices=TYPE_CHOICES,
        help_text="Choose your type of art.",
        )
    description = models.TextField(
        help_text="Describe your artwork in your own words. What are your thoughts and what's the intention behind your masterpiece.",
        null=True,
        blank=True,
    )
    is_stage = models.BooleanField(
        default=True,
    )
    is_showroom = models.BooleanField(
        default=False,
    )
