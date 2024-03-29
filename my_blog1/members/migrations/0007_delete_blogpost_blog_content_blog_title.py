# Generated by Django 4.2.9 on 2024-01-23 09:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_blogpost_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
