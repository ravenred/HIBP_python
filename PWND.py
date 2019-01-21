import requests
import json

headers = {
    'user-agent': 'PWND-Python-tool'
}


def request_email():

    email = input("Please enter your email:\n")

    url = "https://haveibeenpwned.com/api/v2/breachedaccount/"

    requested_email = url+email

    try:
        r = requests.get(requested_email, headers=headers)

        print("Email Address PWND")
        response = json.loads(r.text)

        # print(response[0])
        print("Account Breached: " + response[0]["Name"])
        print("Associated Domain: " + response[0]["Domain"])
        print("Breach Date: " + response[0]["BreachDate"])
        print("Potential Comprised Data: ")
        for i in response[0]["DataClasses"]:
            print("-"+i)

        print("Breach Information: " + response[0]["Description"])

    except json.decoder.JSONDecodeError:

        print("Email Address has not been PWND")


request_email()
