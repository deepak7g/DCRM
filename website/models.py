from django.db import models

# Create your models here.

# class dcrmDb(models.Model):
#     dateCreated = models.DateTimeField(auto_now_add = True)
#     firstName = models.CharField(max_length=100)
#     lastName =  models.CharField(max_length=100)
#     email = models.EmailField(max_length = 100)
#     phoneNo = models.CharField(max_length = 15)
#     address = models.CharField(max_length=250)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     pinCode = models.CharField(max_length=10)

    
#     def __str__(self):
#         return(f"{self.firstName} {self.lastName}")


class dcrmDb2(models.Model):
    dateCreated = models.DateTimeField(auto_now_add = True)
    firstName = models.CharField(max_length=100)
    lastName =  models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    phoneNo = models.CharField(max_length = 15)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pinCode = models.CharField(max_length=10)

    
    def __str__(self):
        return(f"{self.firstName} {self.lastName}")