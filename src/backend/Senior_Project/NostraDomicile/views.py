import mysql.connector
from django.http import HttpResponse
from django.shortcuts import render
from NostraDomicile.models import HomeData

def test(request):
	db = mysql.connector.connect(user='ctsimaan', password='SeniorProject490', host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com', database='PyZillow_Data')
	cursor = db.cursor()
	cursor.execute('SELECT * FROM `PyZillow_Data`.`home_data` LIMIT 5')
	text = '<html><head><style>tr { border: 1px solid black; }</style></head><body><table cellspacing="5" cellpadding="5" style="border:1px solid black; border-collapse:collapse;"><tr>'
	for i in range(len(cursor.description)):
		text += '<th>' + str(cursor.description[i][0]) + '</th>'
	text += '</tr>'
	for row in cursor.fetchall():
		text += '<tr>'
		for column in row:
			text += '<td>' + str(column) + '</td>'
		text += '</tr>'
	text += '</table></body></html>'
	db.close()
	return HttpResponse(text)

def index(request):
	return render(request, 'index.html')
