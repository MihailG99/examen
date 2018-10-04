from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    last_name = models.CharField(max_length=150, db_index=True)
    number_of_login = models.IntegerField()

    def __str__(self):
        return self.first_name