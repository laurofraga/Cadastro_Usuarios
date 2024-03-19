from django.db import models

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome =models.TextField(max_length=225)
    data_nasc =models.DateField()
    sexo = models.CharField(max_length=10)
    email = models.EmailField(default='example@email.com')
    