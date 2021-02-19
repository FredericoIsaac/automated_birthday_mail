import datetime as dt
import smtplib
import random
import pandas as pd


MY_MAIL = "fake_mail@gmail.com"
PASSWORD = "fake_password"

# Get birthday contacts
birthdays_data = pd.read_csv("birthdays.csv")

# Get current date
now = dt.datetime.now()

# Filter people that do birthday today
today_birthday = birthdays_data[(birthdays_data["month"] == now.month) & (birthdays_data["day"] == now.day)]

names = today_birthday.name

for index in range(len(today_birthday)):
    name = today_birthday.values[index][0]
    to_mail = today_birthday.values[index][1]

    letter_number = random.randint(1, 3)

    with open(f"./letter_templates/letter_{letter_number}.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Encrypt mail
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL,
                                to_addrs=to_mail,
                                msg=f"Subject:Happy Birthday!!\n\n{new_letter}")





