# Generated by Django 4.0.5 on 2022-08-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourusers', '0002_remove_userprofile_external_link_userprofile_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(db_index=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
