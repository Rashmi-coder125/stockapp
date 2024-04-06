from django.shortcuts import render, redirect
from .models import Item, Category
from .forms import ItemForm, CategoryForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Or where you want to redirect after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
@login_required    
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # or another appropriate view
    else:
        form = CategoryForm(instance=category)
    return render(request, 'stockapp/update_category.html', {'form': form})

@login_required
def delete_item_confirm(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')  # Redirect to the item list or home page after deletion
    return render(request, 'stockapp/delete_item_confirm.html', {'item': item})


def home(request):
    return render(request, 'stockapp/home.html')

@login_required    
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')
    else:
        form = CategoryForm()
    return render(request, 'stockapp/add_category.html', {'form': form})

@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'stockapp/item_list.html', {'items': items})

@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'stockapp/add_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'stockapp/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, pk):
    Item.objects.get(id=pk).delete()
    return redirect('item_list')