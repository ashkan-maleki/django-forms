from django import forms

class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 1', max_length=100)
    size=forms.ChoiceField(label='size', choices=[
        ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')
    ])