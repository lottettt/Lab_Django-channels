from django.shortcuts import render
from .models import Statistic, Dataitem

# Create your views here.
def main(request):
    qs = Statistic.objects.all()
    return render(request, 'main.html', {'qs': qs})

def dashboard(request, slug):
    return render(request, 'dashboard.html', {})