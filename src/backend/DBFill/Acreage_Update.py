import mysql.connector

def Test(adr):
 
    combo = adr.split(',')    
    address = combo[0]
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    print(address)  
    query = 'SELECT `home_data`.`lot_size_sq_footage`\nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`street_address` = %s'
    cursor.execute(query,(address,))
    
    testable = str(cursor.fetchone())[1:-2]
    print(testable)
    

    #sq_ft = str(cursor.fetchone())[3:-3]
    #print(sq_ft)
    
    cnx.commit()
    cursor.close()
    cnx.close()
    

def Update_Lot_Size(adr):
    ## Method to update lot sizes from square feet to acres, rounded down. Goal is to avoid
    ## potential NaN or infinity error when RF runs on the server
    
    combo = adr.split(',')    
    address = combo[0]
    print(address)
    sq_ft = combo[1]
    print(sq_ft)
    lot_size = int(sq_ft)
    
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()   
     
    #query = 'SELECT `home_data`.`lot_size_sq_footage`\nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`street_address` = %s'
    #cursor.execute(query,(address,))
    #sq_ft = str(cursor.fetchone())[1:-2]
    #43560ft per acre
    fPa = 43560  
    acres = lot_size/fPa
    
    print(acres)  
    
    update_query ='UPDATE `PyZillow_Data`.`home_data`\nSET`home_data`.`lot_size_sq_footage` = %s\nWHERE `home_data`.`street_address` = %s'
    cursor.execute(update_query,(acres,address))
    cnx.commit()
    cursor.close()
    cnx.close()
    

file1 = open("C:\Users\Christian\Documents\LiClipse Workspace\Example1\Example1\ALL.csv", "r+")
list1 = file1.read().split('\n')

i = len(list1)
j = 0

while j < i:
    Update_Lot_Size(list1[j])
    #Test(list1[j])
    j+=1



