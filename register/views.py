from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmployeeSerializer

# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    
    return render(request, "register/employee_list.html", context)



def employee_form(request, id=0):  #for create and update employee
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id) #get the corresponding id to update
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST) #for create
        else:
            employee = Employee.objects.get(pk=id) #for update
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')



def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

# API VIEWS
class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def perform_create(self, serializer):
        fullname = serializer.validated_data.get('fullname')
        mobile = serializer.validated_data.get('mobile')
        position = serializer.validated_data.get('position')
        
        Employee.objects.create(fullname=fullname, mobile=mobile, position=position)
    
    
    
employee_list_create_api = EmployeeListView.as_view()

# product delete API View
class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)
    
employee_destroy_api = EmployeeDeleteAPIView.as_view()
    
    