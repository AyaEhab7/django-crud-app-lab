from django.shortcuts import render, redirect
from .models import Car 
from .forms import ReservationForm

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# AUTH
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
# def home(request):
#     return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


#about page
def about(request):
    return render(request, 'about.html')

# Fetch all car data from the database
@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user) 
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)  # Get the car object by its ID
    reservation_form = ReservationForm()
    return render(request, 'cars/detail.html', {
        'car': car, 'reservation_form': reservation_form
    })

# add-reservation
@login_required
def add_reservation(request, car_id):
    form = ReservationForm(request.POST)
    if form.is_valid():
        new_reservation = form.save(commit=False)
        new_reservation.car_id = car_id
        new_reservation.save()
    return redirect('car-detail', car_id=car_id)


# CBVs
class CarCreate(CreateView):
    model = Car
    fields = ['name', 'model', 'price', 'description', 'year']
    success_url = '/cars/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'model', 'price', 'description', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

    


