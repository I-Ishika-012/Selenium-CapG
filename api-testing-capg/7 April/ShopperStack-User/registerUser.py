import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com/shopping"

#json payload as req that we  will send
payload = {
    "city": "London",
    "country": "UK",
    "email": "userhoon@gmail.com",
    "firstName": "Userhoon",
    "gender": "MALE",
    "lastName": "Londonse",
    "password": "userhoon",
    "phone": 9998887776,
    "state": "UK",
    "zoneId": "ALPHA"
}

#headers
headers = {
    "Content-Type": "application/json",
}

#post req to create user
# response = requests.post( f"{base_url}/shoppers", headers=headers, data=json.dumps(payload), verify=False )
#
# #return response
# print(response.status_code)
# print(response.json())


#using session -- std practice
with requests.Session() as session:
    session.headers.update(headers)

    # POST to register
    response = session.post(f"{base_url}/shoppers", json=payload, verify=False)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
