# Generated by Django 3.2.5 on 2022-01-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(blank=True),
        ),
    ]
