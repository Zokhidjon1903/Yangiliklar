from django.shortcuts import render

def index(request):
    return render(request, 'yangiliklar/index.html')

# Create your views here.
