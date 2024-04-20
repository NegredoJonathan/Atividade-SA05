from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    nascimento = models.DateTimeField()
    email = models.CharField(max_length=100)
    countryToWork = models.CharField(max_length=100)

    class Meta:
        db_table = "user"