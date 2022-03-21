from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    # When the add_item form is posted, then run this if statement
    if request.method == "POST":
        form  = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # The following class from forms.py can be used to build the form
    form = ItemForm()
    context = {
        'form': form
        }
    return render(request, "todo/add_item.html", context)


def edit_item(request, item_id):
    # get an instance of the item with the passed in item_id
    item = get_object_or_404(Item, id=item_id)
    # code below updates the item
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # create instance of the ItemForm
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')