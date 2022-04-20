from django.db import models

# Create your models here.

# consider class as tables

# table position 
class Position(models.Model):
    title = models.CharField(max_length=50)

# table employee
class Employee(models.Model):
    # define the columns of the table
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE) # foreign key must reference the corresponding model, the on delete cascade ensures when you delete in position table, the employee table will be deleted as well
    
