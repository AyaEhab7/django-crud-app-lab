from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


class Car:
    def __init__(self, name, model, price, description, year):
        self.name = name
        self.model = model
        self.price = price
        self.description = description
        self.year = year

# Create a list of car instances
cars = [
    Car('Toyota Camry', 'Sedan', 40, 'Comfortable and reliable.', 2022),
    Car('Honda Civic', 'Compact', 30, 'Fuel-efficient and affordable.', 2021),
    Car('BMW X5', 'SUV', 90, 'Luxury and performance combined.', 2023),
    Car('Tesla Model S', 'Electric', 120, 'Cutting-edge electric car.', 2024)
]

#home page
def home(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')

# list of cars
def car_index(request):
    return render(request, 'cars/index.html', {'cars': cars})
