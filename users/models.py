from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name