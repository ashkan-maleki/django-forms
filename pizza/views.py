from django.shortcuts import render
from django.forms import formset_factory

from .forms import PizzaForm, MultiplePizzaForm


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    form = PizzaForm()
    context = {
        'pizzaform': form,
        'multiple_form': multiple_form
    }
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = f'Thanks for ordering! Your ' \
                   f'{filled_form.cleaned_data["size"]} ' \
                   f'{filled_form.cleaned_data["topping1"]} ' \
                   f'and ' \
                   f'{filled_form.cleaned_data["topping2"]} ' \
                   f'pizza is on its way'
            context.update({'note': note})

    return render(request, 'pizza/order.html', context)


def pizzas(request):
    number_of_pizzas = 2
    filled_multipe_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multipe_pizza_form.is_valid():
        number_of_pizzas = filled_multipe_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    context = {'formset': formset}

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Order was not created, please try again'

        context.update({
            'note': note,
        })
        return render(request, 'pizza/pizzas.html', context)
    else:
        return render(request, 'pizza/pizzas.html', context)