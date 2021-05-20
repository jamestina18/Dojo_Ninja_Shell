from django.db import models

# Create your models here.
class Dojo(models.Model):
     name = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     state = models.CharField(max_length=3)

     description =  models.TextField(default="")

     def __str__ (self):
          return f"{self.name} {self.city} {self.state}"

class Ninja(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     dojo_id = models.ForeignKey(Dojo, related_name="ninja", on_delete= models.CASCADE)

     def __str__ (self):
          return f"{self.first_name} {self.last_name}"