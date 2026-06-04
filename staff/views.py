from django.shortcuts import render
from myapp.models import Restaurant
from staff.models import Owner, Employee

def owners_list(request):
    owners = Owner.objects.all()
    return render(request, 'staff/owners_list.html', {'owners': owners})

def employees_by_restaurant(request):
    search_query = request.GET.get('restaurant_name', '')
    employees = None
    selected_restaurant = None

    if search_query:
        selected_restaurant = Restaurant.objects.filter(title__icontains=search_query).first()
        if selected_restaurant:
            employees = Employee.objects.filter(restaurant=selected_restaurant)

    return render(request, 'staff/employees_list.html', {
        'employees': employees,
        'search_query': search_query,
        'restaurant': selected_restaurant
    })