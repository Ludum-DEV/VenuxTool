import requests
import os
import json
import random

logo = """

\033[0;31m ██▒   █▓▓█████  ███▄    █  █    ██ ▒██   ██▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
\033[1;31m▓██░   █▒▓█   ▀  ██ ▀█   █  ██  ▓██▒▒▒ █ █ ▒░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
\033[0;31m ▓██  █▒░▒███   ▓██  ▀█ ██▒▓██  ▒██░░░  █   ░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
\033[1;31m  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░ ░ █ █ ▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
\033[0;31m   ▒▀█░  ░▒████▒▒██░   ▓██░▒▒█████▓ ▒██▒ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
\033[1;31m   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
\033[0;31m   ░ ░░   ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░░   ░▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
\033[1;31m     ░░     ░      ░   ░ ░  ░░░ ░ ░  ░    ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
\033[0;31m      ░     ░  ░         ░    ░      ░    ░                  ░ ░      ░ ░      ░  ░
\033[1;31m     ░                                                                             \033[0m
"""

while True:
    os.system("title VenuxTool")
    os.system("cls")   
    print(logo)
    print("\033[0;31m─────────────────────────────────────────────────────────────────────────────\033[0m")
    print("\033[0;31m─────────────────────────────────────────────────────────────────────────────\033[0m")
    print("")
    print("")
    print("\033[1m\033[1;30m[1] IP Geolocator   \033[1m\033[1;30m[2] Webhook Spammer")
    print("\033[1m\033[1;30m[3] Show HWID       \033[1m\033[1;30m[4] Webhook Info Gatherer")
    print("\033[1m\033[1;30m[5] Playfab Spammer \033[1m\033[1;30m[6] Webhook Deleter")
    print("")
    x = input("\033[1;30mOption: ")


    if x == "1":
        os.system("cls")
        print("IP Geolocator\n")
        ip = input("Enter IP Address: \033[1m\033[1;30m")
        os.system("cls")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("Results:\n")
        print(f"Status: {data['status']}")
        print(f"Entered IP: {data['query']}")
        print(f"ISP: {data['isp']}")
        print(f"Region: {data['regionName']}")
        print(f"Region Code: {data['region']}")
        print(f"Country: {data['country']}")
        print(f"Country Code: {data['countryCode']}")
        print(f"City: {data['city']}")
        print(f"Zip Code: {data['zip']}")
        print(f"Time Zone: {data['timezone']}")
        print(f"Longitude: {data['lon']}")
        print(f"Latitude: {data['lat']}")
        print("\033[0;31mWARNING:\033[0m\033[1;31mUSE THIS INFO RESPONSIBLY!\033[0m")
        print("")
        input("Press Any Key To Return Home")
    
    if x == "2":
        os.system("cls")
        print("Webhook Spammer\n")
        url = input("[REQUIRED] Enter Webhook URL: \033[1m\033[1;30m")
        avatar = input("[REQUIRED] Enter Webhook Avatar URL: \033[1m\033[1;30m")
        name = input("Enter Webhook Name: \033[1m\033[1;30m")
        message = input("Enter Webhook Message: \033[1m\033[1;30m")

        data = {
            "avatar_url": avatar,
            "content": message,
            "username": name
        }
        while True:

            try:
                r = requests.post(url, json=data)
                print("Webhook Successfully Sent!")
            except:
                print("\033[0;31mError Sending Message:\033[0m Did You Input The Correct URL?")

    if x == "3":
        os.system("cls")
        print("Show HWID\n")
        print("CPU Serial: ")
        print(os.system("wmic cpu get ProcessorID"))
        print("Disk Serial: ")
        print(os.system("wmic diskdrive get SerialNumber"))
        print("Motherboard Serial: ")
        print(os.system("wmic baseboard get SerialNumber"))
        input("Press Any Key To Return Home")

    if x == "4":
        os.system("cls")
        print("Webhook Info Gatherer\n")
        url2 = input("Enter Webhook URL: \033[1m\033[1;30m")
        os.system("cls")
        r = requests.get(url2)
        data = r.json()
        url = data.get("url")
        token = data.get("token")
        name = data.get("name")
        id = data.get("id")
        channel_id = data.get("channel_id")
        guild_id = data.get("guild_id")

        print(f"Name: {name}")
        print(f"Token: {token}")
        print(f"ID: {id}")
        print(f"Channel ID: {channel_id}")
        print(f"Guild ID: {guild_id}")
        print(f"URL: {url}")
        print("")
        input("Press Any Key To Return Home")

    if x == "5":
        
        os.system("cls")
        print("Playfab Spammer\n")
        titleid = input(str("Enter Title ID: \033[1m\033[1;30m"))

        while True:
            customid = random.randint(1000, 900000)

            header = {
                "Content-Type": "Application/json"
            }
            body = {
                "TitleId": titleid,
                "CustomId": customid,
                "CreateAccount": True
            }

            try:
                post = requests.post(f"https://{titleid}.playfabapi.com/Client/LoginWithCustomID", json=body, headers=header)
                print("Created Account Successfully!")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

    if x == "6":
        os.system("cls")
        print("Webhook Deleter\n")
        url3 = input("Enter Webhook URL: \033[1m\033[1;30m")
        try:
            delete = requests.delete(url3)
            print("Webhook Deleted Succesfully!")
        except:
            print("\033[0;31mError Deleting Webhook:\033[0m Did You Input The Correct URL?")



    else:
        os.system("cls")
        print("Invalid Option")
        input("Press Any Key To Return Home")