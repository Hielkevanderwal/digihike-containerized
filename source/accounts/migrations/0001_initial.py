# Generated by Django 4.2.13 on 2024-07-11 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_description', models.TextField()),
                ('team_members', models.ManyToManyField(related_name='participating_in_team', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
