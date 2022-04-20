from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__' #get all the fields from model
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        