from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def home (request):
    return HttpResponse ("HELLO FROM THE CORE")

def about (request):
    return HttpResponse ("About page")

def greet(request):
    return render(request, 'core/greet.html', {'name': 'John Doe'})

def note_list (request):
    notes = Note.objects.all()
    return render(request, 'core/note_list.html', {'notes': notes})

def create_note (request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create (title=title, content=content)
        return redirect ('note_list')
    
    return render (request, 'core/create_note.html')
