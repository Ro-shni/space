from django.shortcuts import render
from django.shortcuts import render,HttpResponse
# Create your views here.
def galaxy(request):
    return render(request,'galaxy.html')
def planets(request):
    return render(request,'planets.html')
def dashboard(request):
    return render(request,'dashboard.html')
def earth(request):
    return render(request,'earth.html')
def venus(request):
    return render(request,'venus.html')
def quiz(request):
    return render(request,'quiz.html')
def puzzle(request):
    return render(request,'puzzle.html')
def games(request):
    return render(request,'games.html')
def learningpath(request):
    return render(request,'learningpath.html')