# Generated by Django 4.1.7 on 2023-04-20 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='juegos',
            name='nombre',
            field=models.TextField(max_length=30),
        ),
    ]
