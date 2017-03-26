from django.http import HttpResponse
from django.shortcuts import render
from NostraDomicile.models import HomeData

def test(request):
	text = HomeData.objects.all()
	return HttpResponse(text)

def index(request):
	return render(request, 'index.html')
