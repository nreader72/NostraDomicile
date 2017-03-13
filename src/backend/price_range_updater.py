'''
Created on Mar 9, 2017

@author: Christian
'''



import mysql.connector

def update_price_range(adr):
    query = "SELECT `home_data`.`last_sale_price`\nFROM`PyZillow_Data`.`home_data`\nWHERE`home_data`.`last_sale_price` <> 'NULL' AND `home_data`.`street_address` = %s"
    
    price_range_iter = 0
    unfound = True
    cur_range = 5000
    
    
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    cursor.execute(query,(adr,))
    
    price = str(cursor.fetchone())[1:-2]
    last_price = int(price)
    
    while unfound:
        if (last_price >= cur_range):
            cur_range += 5000
            price_range_iter += 1
        else:
            unfound = False
    
    print(str(last_price) + " : " + str(price_range_iter))
    update_query ='UPDATE `PyZillow_Data`.`home_data`\nSET`home_data`.`price_range` = %s\nWHERE `home_data`.`street_address` = %s'
    cursor.execute(update_query,(price_range_iter,adr))
    cnx.commit()
    cursor.close()
    cnx.close()
        
            
    
    
file1 = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/Complete List.txt", "r+")
list1 = file1.read().split('\n')

i = len(list1)
j = 0

while j < i:
    update_price_range(list1[j])
    j+=1



