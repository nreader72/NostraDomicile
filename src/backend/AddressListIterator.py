
import mysql.connector, time
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails, ZillowError 


## Put addresses into list for processing ##
## Use 'split' to determine delimiting character, if csv, change \n to , ##
address_file = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/27401.txt","r")
address_list = address_file.read().split('\n')

## Add file listing zip codes we have address files for, separate each zip into separate file
## and we can iterate through zipcodes in the list as variables to plug in here where needed
## For the time being, zip codes and zip files are hard coded
## zip_file = open()

## Check boolean used to determine if basic property information are available ##
check = True
## upd boolean used to determine if updated property details are available ##
upd = True

## Configure query for data loading into DB ##

def check_duplicates(address):
    dupe = False
    query = 'SELECT `home_data`.`street_address`\nFROM `PyZillow_Data`.`home_data`\nWHERE `home_data`.`street_address` = %s'

    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    cursor.execute(query,(address,))
    
    init = str(cursor.fetchone())
    street_address = init[3:-3]
    print street_address
    
    if (street_address == address):
        dupe = True
        
    cursor.close()
    cnx.close()
    return dupe

def insert_home(street_address,zip_code,city,state,home_type,
bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,
year_updated,number_of_floors,parking_type,heating_sources,heating_system,
floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,
last_sold_date,last_sale_price,appliances,roof_type,room_types,updated_properties):

    query ='INSERT INTO `PyZillow_Data`.`home_data`(`street_address`,`zip`,`city`,`state`,`home_type`,`bedrooms`,`bathrooms`,`finished_sq_footage`,`lot_size_sq_footage`,`year_built`,`year_updated`,`number_of_floors`,`parking_type`,`heating_sources`,`heating_system`,`floor_covering`,`number_of_rooms`,`neighborhood`,`school_district`,`sold_binary`,`last_sold_date`,`last_sale_price`,`appliances`,`roof_type`,`room_types`,`updated_properties`) \n VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
             
    args = (street_address,zip_code,city,state,home_type,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,year_updated,number_of_floors,parking_type,heating_sources,heating_system,floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,last_sold_date,last_sale_price,appliances,roof_type,room_types,updated_properties)
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    cursor.execute(query,args)
    cnx.commit()
    cursor.close()
    cnx.close()

def insert_partial(street_address,zip_code,city,state,home_type,
bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,sold_binary,updated_properties):

    query ='INSERT INTO `PyZillow_Data`.`home_data`(`street_address`,`zip`,`city`,`state`,`home_type`,`bedrooms`,`bathrooms`,`finished_sq_footage`,`lot_size_sq_footage`,`year_built`,`year_updated`,`number_of_floors`,`parking_type`,`heating_sources`,`heating_system`,`floor_covering`,`number_of_rooms`,`neighborhood`,`school_district`,`sold_binary`,`last_sold_date`,`last_sale_price`,`appliances`,`roof_type`,`room_types`,`updated_properties`) \n VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
    args = (street_address,zip_code,city,state,home_type,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,sold_binary,updated_properties)
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',database='PyZillow_Data')
    cursor = cnx.cursor()
    cursor.execute(query,args)
    cnx.commit()
    cursor.close()
    cnx.close()

def main():
    ## Zillow API call setup ##
    API_KEY = 'X1-ZWz1fmcredpjpn_76gmj'
    zillow_data = ZillowWrapper(API_KEY)
    
    ## variable setup for iteration through address list (from file) ##
    i = 0
    while i < len(address_list):
        ## check used to determine if ds_result raised an exception - no data
        check = True
        ## upd used to determine if upd_result raised an exception - no data
        upd = True
        
        address = address_list[i]
        if(check_duplicates(address)):
            i+=1
            exit
        else:
            ## First API call using address/zip ##
            try:    
                ds_response = zillow_data.get_deep_search_results(address,'27401')
                ds_result = GetDeepSearchResults(ds_response)
            except (ZillowError,UnicodeEncodeError):
                print('No basic property details for:' + address)
                check = False
            finally:
                exit
        
            ## If first API call successful, additional details sought from 2nd API call
            if check:
                try:
                    upd_response = zillow_data.get_updated_property_details(ds_result.zillow_id)
                    upd_result = GetUpdatedPropertyDetails(upd_response)
                except (ZillowError,UnicodeEncodeError):
                    print('No updated property details for:' + address )
                    upd = False
                finally:
                    exit
        
            ## Compares sold date vs. current date to determine "sold" binary status
            ## Older date is "less than" for Python comparison ##
            ## We treat anything sold more than 1 year ago as "unsold" ##
                
            if check:
                if upd:
                    t = 1    
                    if str(upd_result.last_sold_date) != 'None':
                        sale_date = time.strptime(str(upd_result.last_sold_date), "%d/%m/%Y")
                        compare_date = time.strptime('02/08/2016',"%d/%m/%Y")
                        if sale_date < compare_date:
                            s = 0
                        else:
                            s = 1
                    else:
                        s = 0
                    insert_home(address,27401,'Greensboro','NC',ds_result.home_type,ds_result.bedrooms,ds_result.bathrooms,ds_result.home_size,ds_result.property_size,ds_result.year_built,upd_result.year_updated,upd_result.num_floors,upd_result.parking_type,upd_result.heating_sources,upd_result.heating_system,upd_result.floor_material,upd_result.num_rooms,str(upd_result.neighborhood),str(upd_result.school_district),s,str(upd_result.last_sold_date),str(upd_result.last_sold_price),upd_result.appliances,upd_result.roof,upd_result.rooms,t)
                else:
                    s = 0
                    t = 0
                    default = None
                    insert_home(address,27401,'Greensboro','NC',ds_result.home_type,ds_result.bedrooms,ds_result.bathrooms,ds_result.home_size,ds_result.property_size,ds_result.year_built,default,default,default,default,default,default,default,default,default,s,default,default,default,default,default,t)                                                                                                                                    
            i += 1
    
                
main()
        
        
## OLD QUERY STATEMENT
## "INSERT INTO home_data(street_address,zip_code,city,price,home_type,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,year_updated,number_of_floors,parking_type,heating_sources,heating_system,floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,last_sold_date,last_sale_price,appliances,roof_type,room_types)"
## 
