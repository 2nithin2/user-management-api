# Generated by Django 5.1.6 on 2025-03-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
