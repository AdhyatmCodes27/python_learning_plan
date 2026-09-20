from api_utility.client import APIClient
client = APIClient(timeout=10)

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    users = client.get(url)

    print("URL:", url)
    print("Type:", type(users))
    print("Number of users:", len(users))
    if isinstance(users, list):
        print("First user:", users[0]["name"])
    else:
        print("Users is not a list object")

def test_get_with_params():
    url = "https://jsonplaceholder.typicode.com/users"

    params = {
        "username": "Bret",
        "email": "Sincere@april.biz"
    }

    users = client.get(url, params=params)

    print("URL:", url)
    print("Users:", users)

def test_get_with_headers():
    url = "https://httpbin.org/headers"

    headers = {
        "X-My-Header": "HelloPython",
        "Accept": "application/json"
    }

    data = client.get(url, headers=headers)
    print("Response:", data)

def test_post():
    url = "https://jsonplaceholder.typicode.com/users"

    user_data = {
        "name": "Adhyatm Mishra",
        "username": "adhy123",
        "email": "adhy@ex.com"
    }

    headers = {
        "Accept": "application/json"
    }

    data = client.post(url, json_data=user_data, headers=headers)
    print(f"Response: {data}")

def test_put():
    url = "https://jsonplaceholder.typicode.com/users/1"

    update_dict = {
        "name": "Adhyatm Updated",
        "email": "new@example.com"
        }

    headers = {
        "Accept": "application/json"
    }

    data = client.put(url, json_data=update_dict, headers=headers)
    print("Response: ", data)

def test_patch():
    url = "https://jsonplaceholder.typicode.com/users/1"

    update_dict = {
        "email": "patched@example.com"
    }

    headers = {
        "Accept": "application/json"
    }

    data = client.patch(url, json_data=update_dict, headers=headers)
    print("Response:", data)


def test_delete():
    url = "https://jsonplaceholder.typicode.com/users/1"

    headers = {
        "Accept": "application/json"
    }

    response = client.delete(url, headers=headers)

    print("Status code:", response.status_code)
    print("Response:", response)

if __name__ == '__main__':
    test_get_users()
    test_get_with_params()
    test_get_with_headers()
    test_post()
    test_put()
    test_patch()
    test_delete()