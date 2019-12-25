from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    context = {'pizzaform': form}
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = f'Thanks for ordering! Your ' \
                   f'{filled_form.cleaned_data["size"]} ' \
                   f'{filled_form.cleaned_data["topping1"]} ' \
                   f'and ' \
                   f'{filled_form.cleaned_data["topping2"]} ' \
                   f'pizza is on its way'
            context.update({'note': note})

    return render(request, 'pizza/order.html', context)
