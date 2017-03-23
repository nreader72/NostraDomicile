from django.http import HttpResponse
from django.shortcuts import render

def test(request):
	text = 'test'
	return HttpResponse(text)

def index(request):
	return render(request, 'static/templates/index.html')
