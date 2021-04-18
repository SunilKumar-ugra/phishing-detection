from django.db import models


# Create your models here.
class Auth(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        print(self.user_name,self.password)
        return self.user_name

