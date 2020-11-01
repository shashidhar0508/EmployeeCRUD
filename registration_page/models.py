from django.db import models

# Create your models here.
class EmpModel(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=40)
    email=models.EmailField()
    econtact=models.CharField(max_length=12)
    class Meta:
        db_table="empmodel"         #db table will have this name