# Generated by Django 5.0.3 on 2024-03-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.DateField()),
            ],
        ),
    ]
