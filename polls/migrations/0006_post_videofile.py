# Generated by Django 2.2.4 on 2019-11-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
