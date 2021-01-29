from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beaches/', views.beaches_index, name='index'),
    path('beaches/<int:beach_id>/', views.beaches_detail, name='detail'),
]