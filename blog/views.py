from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', context={"title": "Simply-D-Street"})

def dashboard(request):
    return render(request, 'dashboard.html', context={"title": "Simply-D-Street"})