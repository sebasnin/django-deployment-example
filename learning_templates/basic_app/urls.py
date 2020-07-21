from django.urls import path
from basic_app import views



urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/',views.other,name='other')
]