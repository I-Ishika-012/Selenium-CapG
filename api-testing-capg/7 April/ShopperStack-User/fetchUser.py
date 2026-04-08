import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com/shopping"

# Read saved credentials
with open("shopper_credentials.json", "r") as f:
    credentials = json.load(f)

shopper_id = credentials.get("shopperId")
token = credentials.get("jwtToken")

# if not shopper_id or not token:
#     raise ValueError("shopperId or jwtToken is missing in shopper_credentials.json")
#
# headers = {
#     "Authorization": f"Bearer {token}"
# }
#
# # GET request to fetch user details
# response = requests.get(
#     f"{base_url}/shoppers/{shopper_id}",
#     headers=headers,
#     verify=False  # skip SSL verification for testing
# )
#
# print("Status Code:", response.status_code)
# try:
#     print("Response JSON:", response.json())
# except Exception:
#     print("Response Text:", response.text)

# Create a session and set Authorization header
with requests.Session() as session:
    session.headers.update({"Authorization": f"Bearer {token}"})

    response = session.get(f"{base_url}/shoppers/{shopper_id}", verify=False)
    print("Status Code:", response.status_code)
    print("Response:", response.json())