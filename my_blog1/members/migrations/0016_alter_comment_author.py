# Generated by Django 4.2.9 on 2024-02-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=255),
        ),
    ]
