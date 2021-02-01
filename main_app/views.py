from django.shortcuts import render, redirect
from .models import Beach
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WaterForm

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
    water_form=WaterForm()
    return render(request, 'beaches/detail.html', {'beach': beach, 'water_form': water_form})

def add_water(request, beach_id):
  form = WaterForm (request.POST)
  if form.is_valid():
      new_water = form.save(commit=False)
      new_water.beach_id=beach_id
      new_water.save()
  return redirect('detail', beach_id=beach_id)

class BeachCreate(CreateView):
    model=Beach
    fields='__all__'
    success_url='/beaches/'

class BeachUpdate(UpdateView):
    model= Beach
    fields=['name', 'location', 'description']

class BeachDelete(DeleteView):
    model= Beach
    success_url= '/beaches/'