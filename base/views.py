from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):
    return render(request, "index.html")



def barberlar(request):
    products = Product.objects.all()

    return render(request, "barberlar.html", {
        "products": products
    })


def bronlarim(request):

    bronlar = Bron.objects.all()

    return render(request, "bronlarim.html", {
        "bronlar": bronlar
    })


def bron(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == "POST":

        mijoz_ismi = request.POST.get("mijoz_ismi")
        sana = request.POST.get("sana")
        vaqt = request.POST.get("vaqt")

        Bron.objects.create(
            mijoz_ismi=mijoz_ismi,
            sartarosh=product,
            sana=sana,
            vaqt=vaqt
        )

        return redirect("bronlarim")
    return render(request, "bron.html", {
        "product": product
    })

def tarix(request):
    return render(request, "tarix.html")


def profil(request):
    return render(request, "profil.html")