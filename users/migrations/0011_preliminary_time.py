# Generated by Django 4.1.3 on 2022-12-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_preliminary_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='preliminary',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
