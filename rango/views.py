from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return render(request, 'rango/about.html')
    return HttpResponse("Rango says here is the about page")

# Create your views here.
