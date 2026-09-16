import json
# import logging
# logging.basicConfig(level=logging.DEBUG)

from api_utility.logger import get_logger
logger = get_logger(__name__)

def load_users(file_path):
    try:
        # logging.info(f"Loading users from {file_path}")
        logger.info(f"Loading users from {file_path}")
        with open(file_path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        # logging.error(f"Users file not found: {file_path}")
        logger.error(f"Users file not found: {file_path}")
        raise

    except json.JSONDecodeError:
        # logging.error(f"Invalid JSON in file: {file_path}")
        logger.error(f"Invalid JSON in file: {file_path}")
        raise

users = load_users('data/users.json')
print(users)
print(type(users))

# 1. Read users.json and print each user’s name:
for user in users:
    print(f"User names are {user['name']}")
    
# 2. Print users who are 30 or older. 
users_above_30_list = [user['name'] for user in users if user['age']>=30]
users_above_30_names = ", ".join(users_above_30_list)
print(f"Users who are 30 and older are: {users_above_30_names}")

# 3. Create a new dictionary
new_dict = {}
new_dict['total_users'] = len(users)
new_dict['cities'] = [user['city'] for user in users]
print(new_dict)

#4. Take your dictionary from Task 3 and write it to: data/summary.json
with open('data/summary.json', 'w') as f:
    json.dump(new_dict, f, indent=4) # .dump() function is used to convert a Python object to a JSON file (serialization)
