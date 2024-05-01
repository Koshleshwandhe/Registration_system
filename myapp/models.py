from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
