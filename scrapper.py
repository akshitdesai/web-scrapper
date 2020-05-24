#!/usr/bin python

'''
importing required dependencies
'''
import os,random,sys,time,argparse,json
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

'''
Argparse to take input file from user at run time
'''
parser = argparse.ArgumentParser(description='To take input file from user')
parser.add_argument('-i','--input', help='Input file name',required=True)
args = parser.parse_args()

url_to_scrap = 'https://www.barchart.com/stocks/quotes/GOOG/competitors'
chromedriver_path = os.getcwd()+'/driver/chromedriver'

def fetch_Competitors_Data():
    '''
    Function scrap the competitors data from given url
    and save it to dictnary and return 

    '''
    browser = webdriver.Chrome(chromepath)
    browser.get(url_to_scrap)

    #Browser need to be fully loaded
    time.sleep(20)

    #soup instance to get page source
    soup = BeautifulSoup(browser.page_source,features="html.parser")
    
    #!important - After getting the data close browser  
    browser.close()

    #finding required data from soup instance that we have created
    soup = soup.find('div',{'class':'bc-datatable'})
    compSymbol = soup.findAll('a',{'data-ng-class':'setTriggeredClass(row)'}) 
    compName = soup.findAll('td',{'class':'symbolName text-left'})

    data = {}
    #traversing from all data that we collected
    for i in range(0,len(compSymbol)):
        Symbol = compSymbol[i].get_text()
        Name = compName[i].find('span',{'data-ng-bind':'cell'}).get_text()
        data[Symbol] = Name

    return data

def get_Required_Data(required_Symbols,all_Competitors_Data):
    '''
    Create json list for only required data
    from All competitors Data 
    and return list of all required competitors datails 
    '''
    required_Details = []

    #trversing from all required Company's Symbol
    for symbol in required_Symbols:

        #stripping Symbols
        symbol = symbol.strip()
        symbol_Data = {}

        if symbol in all_Competitors_Data:
            #if symbol found then add data from all competitors list
            symbol_Data = {
                "Symbol": symbol,
                "Name": all_Competitors_Data[symbol]
            }

        else:
            #if symbol not found the save as Not found
            symbol_Data = {
                "Symbol": symbol,
                "Name": 'Not found'
            }
        required_Details.append(symbol_Data)

    return required_Details

def read_Input_File(filename):
    '''
    open specified file retuens lines of it  
    '''
    input_file = open(filename, 'r') 
    lines = input_file.readlines()

    #!important - clode the file after reading from it
    input_file.close()
    return lines 

def write_Outputfile(filename,data):
    '''
    take data and dump into json and write in specified file  
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Take file name from arguments
filename = args.input

# Get All symbol from input file
required_Symbols = read_Input_File(filename)

# Fetch All data from given url
all_Competitors_Data = fetch_Competitors_Data()

# Get required data from all data
required_Competitors_Data = get_Required_Data(required_Symbols,all_Competitors_Data)

# Print data in json format
print(required_Competitors_Data)

# write required data into data.json
write_Outputfile('data.json',required_Competitors_Data)

print("\nOutput saved in file:- data.json")




