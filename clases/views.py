"""Views de app clases"""

#Django
from django.shortcuts import render

def horario(request):
    return render(request, 'horario.html')

