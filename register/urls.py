from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #get and post req. for insert operation
    path('<int:id>/', views.employee_form, name="employee_update"), #get and post req. for update operation
    path('list/', views.employee_list, name="employee_list"), #get req. to retrieve and display the records
]