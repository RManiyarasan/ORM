# Ex02 Django ORM Web Application
## Date: 26-10-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-10-26 204658.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin 
from.models import Loan,LoanAdmin
admin.site.register(Loan,LoanAdmin)

models.py

from django.db import models
from django.contrib import admin
class Loan(models.Model):
        Name=models.CharField(max_length=10)
        Accountno=models.IntegerField(primary_key="Refno")
        Address=models.CharField(max_length=30)
        Aadharno=models.IntegerField()
        Email=models.EmailField()
class LoanAdmin(admin.ModelAdmin):
         list_display=('Name','Accountno','Address','Aadharno','Email')
```


## OUTPUT
![alt text](<Screenshot 2024-10-26 202252.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully.
