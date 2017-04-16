#import mysql
import mysql.connector
import json
#import pandas as pd
#import numpy as np
#import plotly.tools as tls
from django.http import HttpResponse
from django.shortcuts import render
from NostraDomicile.models import HomeData
#from rfLoad import Classify

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
	version = '0.78'
	if request.method == 'POST':
		response_data = {}
		response_data['status'] = 'True'
		response_data['zip'] = 'True'
		response_data['factors'] = 'False'
		response_data['message'] = 'Your housing information has successfully been submitted!'
		response_data['zipCode'] = request.POST['zipCode']
		response_data['session'] = '???'
		
		#return render(request, 'index.html', {'version': version, 'status': status, 'message': message, 'zipCode': zipCode, 'session': session})
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return render(request, 'index.html', {'version': version})
def rf(request):
	text = 'hi' #classify("28205.txt")
	return HttpResponse(text)
