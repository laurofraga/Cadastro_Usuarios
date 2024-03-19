# Generated by Django 5.0.3 on 2024-03-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=225)),
                ('data_nasc', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
