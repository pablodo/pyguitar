from django.shortcuts import render
from pyguitar.apps.guitar.board import notes
from pyguitar.apps.guitar.scales import scales

def index(request):
    args = {'notes': notes, 'scales': scales}
    return render(request, 'home.html', args)
