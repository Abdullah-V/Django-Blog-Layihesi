# Generated by Django 3.0.7 on 2020-06-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='elebele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ele1', models.CharField(max_length=40)),
                ('ele2', models.TextField()),
                ('ele3', models.TextField()),
                ('tarih', models.DateTimeField()),
            ],
        ),
    ]
