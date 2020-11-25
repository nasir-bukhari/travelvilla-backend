from django.db import models

# Create your models here.


class UserProfile(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    eMail = models.EmailField(max_length=40, unique=True)
    passWord = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName

