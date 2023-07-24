from django.shortcuts import render, redirect
from .models import *
from .forms import ChoiceForm
import random
import numpy as np

def home(requests):
    ctg = Category.objects.all()
    wear = Wear.objects.all()
    reklama = Reklame.objects.all()
    random_wear = random.choice(reklama)
    ctx = {
        'ctg': ctg,
        "wear": wear,
        "random_wear": random_wear
    }
    return render(requests, 'blog/index.html', ctx)

def contact(requests):
    ctx = {}
    return render(requests, 'blog/contact.html', ctx)

def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    wear = Wear.objects.all().filter(type_id=category.id)
    ctx = {
        "ctg": ctg,
        "category": category,
        "wear": wear
    }
    return render(requests, 'blog/products.html', ctx)


def register(requests):
    ctx = {}
    return render(requests, 'blog/register.html', ctx)


def single(requests, pk=None):
    ctg = Category.objects.all()
    product_pk = Wear.objects.get(pk=pk)
    wear = Wear.objects.all()
    random_w = np.random.choice(wear, size=3, replace=False)
    form = ChoiceForm()
    if requests.POST:
        forms = ChoiceForm(requests.POST or None, requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg':ctg,
        'product_pk': product_pk,
        'form': form,
        'wear': wear,
        'random_w': random_w
    }
    return render(requests, 'blog/single.html', ctx)



def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Yangi foydalanuvchini "User" modeliga qo'shish
        user = User.objects.create(name=name, email=email, phone=phone)
        user.save()

        # Bazaga malumot qo'shildiktan so'ng, foydalanuvchini boshqa sahifaga yo'naltirish
        return redirect('home')  # 'success' nomli URLga o'tish
    else:
        return render(request, 'blog/registr.html')
