# Generated by Django 4.2.9 on 2024-01-29 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_blog_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.category'),
            preserve_default=False,
        ),
    ]