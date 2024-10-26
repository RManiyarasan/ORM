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