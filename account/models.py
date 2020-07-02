from django.db import models

# Create your models here.
class Laptop(models.Model):
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    rating = models.FloatField()
    no_rating = models.IntegerField()
    mrp = models.IntegerField()
    price = models.IntegerField()
    less = models.IntegerField()
    l1 =models.CharField(max_length=200)
    l2 =models.CharField(max_length=200)
    l3 =models.CharField(max_length=200)
    l4 =models.CharField(max_length=200)
    l5 =models.CharField(max_length=200)
    Screen_Size = models.CharField(max_length=50)
    Maximum_Display_Resolution = models.CharField(max_length=50)
    Item_Weight = models.CharField(max_length=50)
    Product_Dimensions = models.CharField(max_length=50)
    Batteries = models.CharField(max_length=100)
    Processor_Brand = models.CharField(max_length=50)
    Processor_Type = models.CharField(max_length=50)
    RAM_Size = models.CharField(max_length=50)
    Memory_Technology = models.CharField(max_length=50)
    Hard_Drive_Size = models.CharField(max_length=50)
    Hard_Disk_Technology = models.CharField(max_length=50)
    Graphics_Coprocessor = models.CharField(max_length=50)
    Operating_System = models.CharField(max_length=50)
    Date_First_Available = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Adduser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email