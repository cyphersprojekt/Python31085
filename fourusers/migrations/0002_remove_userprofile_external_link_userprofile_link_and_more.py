# Generated by Django 4.0.5 on 2022-08-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='external_link',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
