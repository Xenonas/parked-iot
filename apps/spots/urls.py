from django.urls import path
from . import views

app_name="spots"
urlpatterns = [
    path('available/', views.availableseats, name="available"),
    path('save/', views.saveseat, name="save"),
    path('change/', views.saveseat, name="change"),
    path('getdata/', views.savedata, name="data")
]