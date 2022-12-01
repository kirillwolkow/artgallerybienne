# Generated by Django 4.1.3 on 2022-12-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AddField(
            model_name='post',
            name='art_type',
            field=models.CharField(blank=True, choices=[('PAI', 'Painting'), ('DRA', 'Drawing'), ('SCU', 'Sculpture'), ('ARC', 'Architecture'), ('LIT', 'Literature'), ('MUS', 'Music'), ('THE', 'Theater'), ('DAN', 'Dance'), ('CIN', 'Cinema')], default='PAI', help_text='Choose your type of art.', max_length=150, verbose_name='art type'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='artworks/%Y/%m/%d/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_showroom',
            field=models.BooleanField(default=True),
        ),
    ]