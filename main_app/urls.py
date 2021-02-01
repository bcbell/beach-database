from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beaches/', views.beaches_index, name='index'),
    path('beaches/<int:beach_id>/', views.beaches_detail, name='detail'),
    path('beaches/create/', views.BeachCreate.as_view(), name='beaches_create'),
    path('beaches/<int:pk>/update/', views.BeachUpdate.as_view(), name='beaches_update'),
    path('beaches/<int:pk>/delete/', views.BeachDelete.as_view(), name= 'beaches_delete'),
    path('beach/<int:beach_id>/beach_water/', views.add_water, name='add_water'),
]