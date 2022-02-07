from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria, Producent


def index(request):
    #wszystkie   = Produkty.objects.all()
    #jeden       = Produkty.objects.get(pk=6)
    #kat         = Produkty.objects.filter(kategoria=1)
    #kat_name    = Kategoria.objects.get(id=1)
    #prod_name   = Producent.objects.get(id=1)
    kategorie   = Kategoria.objects.all()
    #null        = Produkty.objects.filter(kategoria__isnull=True)
    #zawiera     = Produkty.objects.filter(opis__icontains='wycieraczki')
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_produkt,
            'kategorie': kategorie}
    return render(request, 'kategoria_produkt.html', dane)

def produkt (request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user, 'kategorie':kategorie }
    return render(request, 'produkt.html', dane)
