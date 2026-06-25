# from django.shortcuts import render
from django.http import HttpResponse

def index():
return HttpResponse("Привет. Вы находитесь на странице с результатами опроса.")

# Create your views here.
