# Generated by Django 4.1.3 on 2022-12-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_stream_alter_profile_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='stream',
            field=models.CharField(max_length=50, null=True),
        ),
    ]