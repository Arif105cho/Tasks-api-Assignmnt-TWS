# Generated by Django 5.0.2 on 2024-03-02 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Inprogress', 'Inprogress'), ('Done', 'Done')], default='Todo', max_length=20),
        ),
    ]
