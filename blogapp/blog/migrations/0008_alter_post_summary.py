# Generated by Django 4.2.13 on 2024-08-01 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
