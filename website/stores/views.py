from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Store
from .forms import StoreForm

@login_required
def stores(request):

    stores = Store.objects.all()

    return render(request, 'stores/stores.html', {
        'stores': stores,
    })

@login_required
def addin_store(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = StoreForm(request.POST)

        if form.is_valid():
            # store = form.save(commit=False)
            form.save()
            return redirect('stores:stores')
    
    else:
        form = StoreForm()

    return render(request, 'stores/add_store.html', {
        'form': form
    })


def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('/')
    
    stores = get_object_or_404(Store, pk=pk)

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=stores)
        if form.is_valid():
            form.save()

            return redirect('stores:stores')
    else:
        form = StoreForm(instance=stores)

    return render(request, 'stores/add_store.html', {
        'form': form
    })


@login_required
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('stores:stores')
    
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('stores:stores')
    

