# Generated by Django 2.1.2 on 2018-10-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landing_page_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=10)),
                ('introduction', models.CharField(default='Your Introduction goes here', max_length=500)),
            ],
        ),
    ]
