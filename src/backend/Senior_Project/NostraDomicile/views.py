#import mysql
import mysql.connector
import json
import pandas as pd
import numpy as np
import csv
#import plotly.tools as tls
from django.http import HttpResponse
from django.shortcuts import render
from NostraDomicile.models import HomeData
from sold_classifier import sold_classifier
from attribute_classifier import attribute_classifier

def test(request):
	db = mysql.connector.connect(user='ctsimaan', password='SeniorProject490', host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com', database='PyZillow_Data')
	cursor = db.cursor()
	query = 'SELECT * \nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`zip` = %s'
	cursor.execute(query,('27358',))
	result = cursor.fetchall()
	list = str(result)
	fp = open('NostraDomicile/test.txt','w+')
	fp.write(list)
	fp.close()
	text = "Test:" + str(sold_classifier('27358'))
	
	
	#cursor.execute('SELECT * FROM `PyZillow_Data`.`home_data` LIMIT 10')
	#text = '<html><head><style>tr { border: 1px solid black; }</style></head><body><table cellspacing="5" cellpadding="5" style="border:1px solid black; border-collapse:collapse;"><tr>'
	#for i in range(len(cursor.description)):
	#	text += '<th>' + str(cursor.description[i][0]) + '</th>'
	#text += '</tr>'
	#for row in cursor.fetchall():
	#for row in result:
	#	text += '<tr>'
	#	for column in row:
	#		text += '<td>' + str(column) + '</td>'
	#	text += '</tr>'
	#text += '</table></body></html>'
	
	db.close()
	
	return HttpResponse(text)

def index(request):
	version = '0.941'
	if request.method == 'POST':
		attributes = attribute_classifier(request.POST['zipCode'])
		output = ''
		for key in request.POST:
			if key != 'csrfmiddlewaretoken':
				if request.POST[key] != '':
					output += key + ': ' + request.POST[key] + ', '
		
		output = output[:-2]

	#	db = mysql.connector.connect(user='ctsimaan', password='SeniorProject490', host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com', database='PyZillow_Data')
	#	cursor = db.cursor()

		

	#	query = 'SELECT * \nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`zip` = %s'
	#	cursor.execute(query,(zCode,))
		
	#	result = cursor.fetchall()
	#	fp = open('test.txt','w+')
	#	testFile = csv.writer(fp)
	#	testFile.writerows(result)
		#reader = csv.reader(fp)
	#	fp.close()
		
		response_data = {}
		response_data['status'] = 'True'
		response_data['zip'] = 'True'
		response_data['factors'] = 'False'
		response_data['message'] = 'Your housing information has been submitted! These are the values you submitted: <br>' + output 
		response_data['attributes'] = str(attributes)

		if request.POST['price'] != '':
			response_data['factors'] = 'True'

		

	#	db.close()
		
		#return render(request, 'index.html', {'version': version, 'status': status, 'message': message, 'zipCode': zipCode, 'session': session})
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return render(request, 'index.html', {'version': version})
def rf(request):
	text = 'hi' #classify("28205.txt")
	return HttpResponse(text)
