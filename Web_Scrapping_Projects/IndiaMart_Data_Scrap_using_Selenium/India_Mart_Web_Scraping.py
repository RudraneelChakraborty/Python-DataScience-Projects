from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import datetime as dt
import pandas as pd
import os

driver = webdriver.Chrome()

#driver.get('https://dir.indiamart.com/search.mp?ss=Saree&prdsrc=1&cq=Kolkata&cityid=70772&stype=attr=1|attrS&res=RC5')
driver.get(input('Give the URL to Scrap:\n '))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

WebDriverWait(driver= driver, timeout=2)

storeDetails = driver.find_elements(By.CLASS_NAME,'clg')
names = driver.find_elements(By.CLASS_NAME,'lcname')
contact_list = driver.find_elements(By.CLASS_NAME,'pns_h')

namelist = []
addresslist = []
numberslist = []

# take all details in append into list, But if storedetails length is not 0::
if len(storeDetails) != 0:
    for i in range(len(names)):
    
        namelist.append(names[i].text)
        addresslist.append(storeDetails[i].text)
        wait = WebDriverWait(driver, 10)
        contact = contact_list[i].get_attribute('innerHTML')
        numberslist.append(contact)

# This is for another scenario, where after searching indiamart that keep classes on different way::::
if len(storeDetails) == 0:
    dirty_addresslist = []
    for i in range(len(names)):
        storeDetails = driver.find_element(By.XPATH,f"//*[@id='citytt{i+1}']/span/p")
        dirty_addresslist.append(storeDetails.get_attribute('innerHTML'))
    addresslist = [address.replace('\n',' ') for address in dirty_addresslist]
    
    for i in range(len(names)):
        namelist.append(names[i].text)
        wait = WebDriverWait(driver, 10)
        contact = contact_list[i].get_attribute('innerHTML')
        numberslist.append(contact)

    
#Create Dictionary out of it
data = {
        'Company/Store Name': namelist,
        'Address':addresslist,
        'Phone Number':numberslist
        }

df = pd.DataFrame(data)

#Check the filename if the file is already exist or not, If exist then that keep increament the number or occurance
file_name = f"India_Mart_Web_Scrapping_{dt.date.today()}.csv"
if os.path.isfile(file_name):
    expand = 1
    while True:
        expand += 1
        new_file_name = file_name.split(".csv")[0] + "_" + str(expand) + ".csv"
        if os.path.isfile(new_file_name):
            continue
        else:
            file_name = new_file_name
            break

#Load the file on same directory
df.to_csv(file_name,header=True)
print(f'Created Filename: {file_name}')
driver.close()


