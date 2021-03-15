import datetime as dt
import pandas as pd
import random
import smtplib
import os

date = dt.datetime.now()
today_tuple = (date.month,date.day)

birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in birthdays_data.iterrows()}

if today_tuple in birthdays_dict:
    random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(random_letter) as letter_file:
        contents = letter_file.read()
        birthday_name = birthdays_dict[today_tuple]["name"]
        contents = contents.replace("[NAME]",birthday_name)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = os.environ.get("GMAIL_EMAIL")
        password = os.environ.get("id_password")

        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today_tuple]["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )



