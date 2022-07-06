# Generated by Django 4.0.5 on 2022-07-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0003_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='replyimgs/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postimgs/'),
        ),
    ]
