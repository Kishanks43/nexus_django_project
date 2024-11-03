from django.db import models

# Create your models here.
class Register(models.Model):
    name= models.CharField(max_length=122)
    srn= models.CharField(max_length=13)
    prn= models.CharField(max_length=13)
    email= models.EmailField(max_length=25)
    reason=models.TextField()
    date= models.DateField()

    def __str__(self) :
        return self.name 