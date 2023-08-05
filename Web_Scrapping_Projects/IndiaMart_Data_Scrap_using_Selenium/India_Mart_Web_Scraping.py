from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import datetime as dt
import pandas as pd
import os

driver = webdriver.Chrome()

#driver.get('https://dir.indiamart.com/bengaluru/laminated-sheet.html')
driver.get(input('Give the URL to Scrap:\n '))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

storeDetails = driver.find_elements(By.CLASS_NAME,'clg')
names = driver.find_elements(By.CLASS_NAME,'lcname')
contact_list = driver.find_elements(By.CLASS_NAME,'pns_h')

namelist = []
addresslist = []
numberslist = []

# take all details in append into the list
for i in range(len(names)):
    namelist.append(names[i].text)
    addresslist.append(storeDetails[i].text)
    wait = WebDriverWait(driver, 10)
    contact = contact_list[i].get_attribute('innerHTML')
    numberslist.append(contact)
    

#Create a Dictionary out of it
data = {
        'Company/Store Name': namelist,
        'Address':addresslist,
        'Phone Number':numberslist
        }

df = pd.DataFrame(data)

#Check the filename if the file already exists or not, If exist then that keep increasing the number or occurrence
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
df.to_csv(file_name,header=False)
print(f'Created Filename: {file_name}')
driver.close()
