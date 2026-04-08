import requests

# payload = {
# "id": 12,
#   "category": {
#     "id": 1,
#     "name": "dog"
#   },
#   "name": "baby doggie",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }

# response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
# return response.json()['id']

# expected_status_code = 200
# actual_status_code = response.status_code
# assert actual_status_code == expected_status_code
# print(response.status_code)
# print(response.text)
# petId = payload.get('id')
#
# res2 = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}')
# print(res2.status_code)



#usinf fn
def manage_pet_lifecycle(pet_id):
    url = 'https://petstore.swagger.io/v2'

    payload = {
        "id": pet_id,
        "category": {"id": 1, "name": "dog"},
        "name": "baby doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }

    # Create the pet
    post_res = requests.post(f"{url}/pet", json=payload)
    print(f"Post Status: {post_res.status_code}")

    # Delete the pet using an f-string
    delete_res = requests.delete(f"{url}/pet/{pet_id}")
    print(f"Delete Status: {delete_res.status_code}")

    return delete_res.status_code


# Usage
manage_pet_lifecycle(12)

