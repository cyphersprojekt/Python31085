# Generated by Django 4.0.5 on 2022-08-30 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fourusers', '0004_userprofile_first_name_userprofile_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_pics')),
                ('link', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
