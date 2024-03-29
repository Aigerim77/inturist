# Generated by Django 3.2.4 on 2021-06-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_coiunt', models.IntegerField(default=0)),
                ('is_publicated', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'места',
                'ordering': ['name'],
            },
        ),
    ]
