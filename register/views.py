from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, "register/employee_list.html")

def employee_form(request):  #for create and update employee
    return render(request, "register/employee_form.html")

def employee_delete(request):
    return
