from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails
from datetime import datetime
import mysql.connector

## Zillow API setup ##
API_KEY = 'X1-ZWz1fmcredpjpn_76gmj'
zillow_data = ZillowWrapper(API_KEY)

## Put (csv) addresses into list for processing ##
address_file = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/Home_Data.txt","r")
address_list = address_file.read().split(',')

## Configure query for data loading into DB ##

def insert_home(street_address,zip_code,city,price,home_type,
bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,
year_updated,number_of_floors,parking_type,heating_sources,heating_system,
floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,
last_sold_date,last_sale_price,appliances,roof_type,room_types):

    query = "INSERT INTO home_data(street_address,zip_code,city,price,home_type,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,year_updated,number_of_floors,parking_type,heating_sources,heating_system,floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,last_sold_date,last_sale_price,appliances,roof_type,room_types)"
    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    args = (street_address,zip_code,city,price,home_type,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,year_updated,number_of_floors,parking_type,heating_sources,heating_system,floor_covering,number_of_rooms,neighborhood,school_district,sold_binary,last_sold_date,last_sale_price,appliances,roof_type,room_types)
    
    cnx = mysql.connector.connect(name='MySQL57',user='root',password='guest',host='VAIO',database='pyzillow_data')
    cursor = cnx.cursor()
    cursor.execute(query,args)
    cnx.commit()
    cursor.close()
    cnx.close()

def main():
    i = 0
    while i < len(address_list):
        address = address_list[i]
        ds_response = zillow_data.get_deep_search_results(address, '27410')
        ds_result = GetDeepSearchResults(ds_response)
        upd_response = zillow_data.get_updated_property_details(ds_result.zillow_id)
        upd_result = GetUpdatedPropertyDetails(upd_response)
        
        ## Older date is "less than" for Python comparison ##
        sale_date = time.strptime(upd_result.last_sold_date, "%d/%m/%Y")
        compare_date = time.strptime('02/08/2016',"%d/%m/%Y")
        
        if sale_date < compare_date:
            s = '0'
        else:
            s = '1'
        
        insert_home(address,'27410','Greensboro','NC',ds_result.home_type,ds_result.bedrooms,ds_result.bathrooms,ds_result.home_size,ds_result.property_size,
        ds_result.year_built,upd_result.year_updated,upd_result.num_floors,upd_result.parking_type,upd_result.heating_sources,upd_result.heating_system,
        upd_result.floor_material,upd_result.num_rooms,str(upd_result.neighborhood),str(upd_result.school_district),s,upd_result.last_sold_date,
        upd_result.last_sold_price,upd_result.appliances,upd_result.roof,upd_result.rooms)
        i += 1
