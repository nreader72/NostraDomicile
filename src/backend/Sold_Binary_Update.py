import mysql.connector
from datetime import datetime as dt

## Uses a text file address list to update tuples where the sold binary value is
## either incorrect because of insertion issues or based on updated data about
## the property

def Update_Sold(adr):
    query = 'SELECT `home_data`.`last_sold_date`\nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`updated_properties` = %s AND `home_data`.`sold_binary` = %s AND `home_data`.`street_address` = %s'
    #addressq = 'SELECT `home_data`.`street_address`\nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`updated_properties` = %s AND `home_data`.`sold_binary` = %s'
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    cursor.execute(query,(1,0,adr))
    
    last_sold = str(cursor.fetchone())[3:-3]
    print(last_sold)
    
    if ((last_sold) != 'None') & (last_sold != 'n') & (last_sold != ''):
        sale_date = dt.strptime(last_sold,"%m/%d/%Y")
        compare_date = dt.strptime('02/08/2016',"%m/%d/%Y")
        if sale_date < compare_date:
            s = 0
        else:
            s = 1
    else:
        s = 0
        
    print(s)
    if (s==1):
        update_query ='UPDATE `PyZillow_Data`.`home_data`\nSET`home_data`.`sold_binary` = %s\nWHERE `home_data`.`street_address` = %s'
        cursor.execute(update_query,(1,adr))
        cnx.commit()
    
    cursor.close()
    cnx.close()
    

file1 = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/adl.txt", "r+")
list1 = file1.read().split('\n')

i = len(list1)
j = 0

while j < i:
    print (list1[j])
    Update_Sold(list1[j])
    j+=1



