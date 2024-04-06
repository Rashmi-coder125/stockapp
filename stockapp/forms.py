from django import forms
from django.core.exceptions import ValidationError
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError("Item name must contain only letters.")
        return name

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        if not isinstance(quantity, int):
            raise ValidationError("Quantity must be a whole number.")
        return quantity

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValidationError("Category name must contain only letters and spaces.")
        return name
