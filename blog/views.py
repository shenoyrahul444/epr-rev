from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog/home.html')

def contact(request):
    vals = {'names': ["Rahul","Urvi","Rekha","Shradda","Mukesh"]}
    # vals = {}

    return render(request,'blog/contact.html', vals)