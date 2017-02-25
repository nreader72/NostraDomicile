'''
Created on Feb 25, 2017

@author: Christian
'''
import AddressListIterator

def ZipIterate(city):
    zip_file = open("C:/Users/Christian/Documents/LiClipse Workspace/Example1/Zip_Code_Lists/" + city + "/" + city + "_Zip_List.txt","r")
    zip_list = zip_file.read().split('\n')  #\,
    i = 0
    
    while i < len(zip_list):
        zip_code = zip_list[i]
        AddressListIterator.main(zip_code,city)
        i+=1


