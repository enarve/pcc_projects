from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzeria/index.html')