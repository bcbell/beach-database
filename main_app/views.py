from django.shortcuts import render
from .models import Beach


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beaches_index(request):
    beaches= Beach.objects.all()
    return render(request, 'beaches/index.html', {'beaches': beaches}) 

def beaches_detail(request, beach_id):
    beach = Beach.objects.get(id=beach_id)
    return render(request, 'beaches/detail.html', {'beach': beach})