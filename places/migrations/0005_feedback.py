# Generated by Django 3.1.3 on 2021-07-07 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0004_auto_20210707_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст обратной связи')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'обратная связь',
                'verbose_name_plural': 'обратные связи',
            },
        ),
    ]
