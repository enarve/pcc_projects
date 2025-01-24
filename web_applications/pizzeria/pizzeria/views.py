from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    "Menu."
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/menu.html', context=context)

def pizza(request, pizza_id):
    "Pizza."
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria/pizza.html', context=context)