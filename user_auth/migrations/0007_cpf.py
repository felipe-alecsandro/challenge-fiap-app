# Generated by Django 3.2.13 on 2023-06-30 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_alter_baseuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cpf',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'CPF',
                'verbose_name_plural': 'CPFs',
            },
        ),
    ]
