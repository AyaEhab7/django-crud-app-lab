from django.shortcuts import render
from django.http import HttpResponse
from .models import Car 


# class Car:
#     def __init__(self, name, model, price, description, year):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.description = description
#         self.year = year

# # Create a list of car instances
# cars = [
#     Car('Toyota Camry', 'Sedan', 40, 'Comfortable and reliable.', 2022),
#     Car('Honda Civic', 'Compact', 30, 'Fuel-efficient and affordable.', 2021),
#     Car('BMW X5', 'SUV', 90, 'Luxury and performance combined.', 2023),
#     Car('Tesla Model S', 'Electric', 120, 'Cutting-edge electric car.', 2024)
# ]

#home page
def home(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')

# list of cars
# Fetch all car data from the database
def car_index(request):
    cars = Car.objects.all()  
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)  # Get the car object by its ID
    return render(request, 'cars/detail.html', {'car': car})
