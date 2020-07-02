from django.db import models

# Create your models here.
class Addcart(models.Model):
    email = models.EmailField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email