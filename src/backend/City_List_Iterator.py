'''
Created on Feb 25, 2017

@author: Christian
'''
import Zip_List_Iterator

def CityIterate():
    city_file = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/Zip_Code_Lists/City_List.txt")
    city_list = city_file.read().split('\n')
    
    i= 5
    while i < len(city_list):
        city = city_list[i]
        Zip_List_Iterator.ZipIterate(city)
        i+=1

CityIterate()