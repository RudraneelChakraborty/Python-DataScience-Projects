import pandas as pd
import datetime as dt
import random as rd
import smtplib

now = dt.datetime.now()
Today_date = now.date()
Today_tuple = (now.month, now.year)

my_email = 'abc@abc.com'
password = 'password'

bday_data = pd.read_csv('birthdays.csv')

bday_dict = {(bday_data["month"] , bday_data["day"]):bday_data for (index,n) in bday_data.iterrows()}

if Today_tuple in bday_dict:
    birthday_person = bday_dict[Today_tuple]

    with open(f'letter_templates/letter_{rd.randint(1,3)}.txt',mode='r',encoding='utf-8') as letter_file:
        email_data = letter_file.read()
        email_data = email_data.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person['email'], 
            msg= f'Subject:Happy BirthDay\n\n{email_data}')
