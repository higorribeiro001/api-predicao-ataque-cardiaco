# Generated by Django 5.0.7 on 2024-07-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
