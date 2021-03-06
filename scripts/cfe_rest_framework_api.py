import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "code-cake.png")

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY4MDI0MzQ1LCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY4MDI0MDQ1fQ.y52y_0cA68ufibbqNoOKGwaowtch_Ik4N5Ol1xx6P7E',
}

data = {
    'username': 'admin9',
    'email': 'admin9@gmail.com',
    'password': 'superuser',
    'password2': 'superuser',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()  # ['token']
print(token)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(
#     REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()  # ['token']

# print(new_token)


# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         "content": "updated description"
#     }

#     json_data = json.dumps(data)
#     posted_response = requests.put(
#         ENDPOINT + str(10) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)


# get_endpoint = ENDPOINT + str(12)


# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)

# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data,
#                                  files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(
#     method='put',
#     data={'id': 13, 'user': 1, "content": "Some new content"},
#     is_json=False,
#     img_path=image_path
# )


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do(data={'id': 500})

# do(method='delete', data={'id': 9})

# do(method='put', data={'id': 7, "content": "changed the content", "user": 1})

# do(method='post', data={"content": "latest content", "user": 1})

# create
# retrieve / list
# update
# delete

# r = requests.request("get", "http://127.0.0.1:8000/api/status/?id=" + str(id), data={'id: 12'})
