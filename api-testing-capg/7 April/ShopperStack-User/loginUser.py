import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com/shopping"

# Replace with your registered user's email and password
login_payload = {
    "email": "userhoon@gmail.com",
    "password": "userhoon",
    "role": "SHOPPER"
}

headers = {"Content-Type": "application/json"}

# POST request to login
# response = requests.post(
#     f"{base_url}/users/login",
#     headers=headers,
#     data=json.dumps(login_payload),
#     verify=False
# )
#
# print("Status Code:", response.status_code)
# print("Response:", response.json())

# Save both shopperId and JWT token for easy reference
# if response.status_code == 200:
#     data = response.json().get("data", {})
#     # Adjust keys if API uses different names
#     token = data.get("jwtToken")
#     shopper_id = data.get("userId")  # or "userId" depending on API
#
#     saved_data = {
#         "shopperId": shopper_id,
#         "jwtToken": token
#     }
#
#     with open("shopper_credentials.json", "w") as f:
#         json.dump(saved_data, f, indent=4)
#
#     print(f"Saved shopperId and JWT token to shopper_credentials.json")


#using session

# Create session
with requests.Session() as session:
    session.headers.update(headers)

    response = session.post(f"{base_url}/users/login", json=login_payload, verify=False)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        token = data.get("jwtToken")  # adjust key if API uses different
        saved_data = {
            "shopperId": data.get("userId"),
            "jwtToken": token
        }
        with open("shopper_credentials.json", "w") as f:
            json.dump(saved_data, f, indent=4)
        print("shopperId and JWT token saved in shopper_credentials.json")