from django.shortcuts import HttpResponse, render
from .models import Employee
# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        mobile = data['phone']

        print("Name : ",name)
        print("Mobile : ",mobile)

        employee = Employee.objects.create(name=name,mobile=mobile)
        print(employee)
    return render(request,'home.html')