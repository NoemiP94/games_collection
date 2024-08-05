from django.shortcuts import render
from .models import Videogame

# Create your views here.
# request contiene i parametri della richiesta dell'utente
def videogame_list(request):
    # restituisce un queryset di tutti gli oggetti
    videogames = Videogame.objects.all()
    # request -> richiesta dati utente
    # file html -> dove devono venire renderizzati
    # {'videogames': videogames} -> dizionario, dati che dobbiamo passare al template
    return render(request, 'videogame_list.html', {'videogames': videogames})