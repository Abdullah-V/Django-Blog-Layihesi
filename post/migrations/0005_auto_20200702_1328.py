# Generated by Django 3.0.7 on 2020-07-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200702_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tarih',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]