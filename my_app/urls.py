from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
#    path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),  # Add the dynamic route
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),

    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('cars/<int:car_id>/add-reservation/', views.add_reservation, name='add-reservation'),
]