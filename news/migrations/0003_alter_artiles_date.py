# Generated by Django 5.0 on 2023-12-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_artiles_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
