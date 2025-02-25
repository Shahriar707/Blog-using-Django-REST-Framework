# Generated by Django 4.2.13 on 2024-06-23 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=500)),
                ('text', models.TextField(max_length=10000)),
                ('main_images', models.ImageField(upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
