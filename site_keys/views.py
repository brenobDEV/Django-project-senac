from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Key
from .forms import KeysForm


def home_view(request):
    return render(request, 'home.html')

def keys_shop(request):
    lista_keys = Key.objects.all()
    form = KeyForm()

    if request.method == 'POST':
        if 'produto_id' in request.POST:
            produto = get_object_or_404(Key, id=request.POST.get('Keys_id'))
            form = KeysForm(request.POST, instance=produto)
        else:
            form = KeysForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('key_shop')

    context = {
        'produtos': lista_keys,
        'form': form,
    }
    
    return render(request, 'keys_shop.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('keys') 

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('keys') 
    else:
        form = UserCreationForm()