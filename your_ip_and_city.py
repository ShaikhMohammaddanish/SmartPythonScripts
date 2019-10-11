#this programm will give your ip adress, location and city

import requests

print("To exicut this programm must turn on internet.")

r=requests.get("https://ipinfo.io/")

r=r.json()

print(f'your ip adress is :- {r["ip"]}\nyour longitude is :- {r["loc"].split(",")[0]}\nlatitude is {r["loc"].split(",")[1]}\nyour city is :- {r["city"]}')


input("Press any key to Quit" )
