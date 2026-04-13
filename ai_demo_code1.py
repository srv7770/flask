import requests

# ❌ Hardcoded secret
API_KEY = "sk-1234567890"


# ❌ Unsafe function (can crash)
def get_user_name(data):
    return data["user"]["profile"]["name"]


# ❌ No error handling + no timeout
def call_external_api():
    url = "http://example.com/api"
    response = requests.get(url)
    return response.json()


# ❌ SQL Injection risk
def get_user_query(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query


# ❌ Redundant logic
def check_value(x):
    if x > 100:
        return True
    else:
        return True


# ❌ Inefficient loop
def find_even_numbers(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result


# ❌ Duplicate logic (redundancy)
def process_a(data):
    result = []
    for d in data:
        if d > 10:
            result.append(d)
    return result


def process_b(data):
    result = []
    for d in data:
        if d > 10:
            result.append(d)
    return result


# ❌ Missing validation
def calculate_discount(price, discount):
    return price - (price * discount / 100)


# ❌ Logging sensitive data
def login(user, password):
    print("User:", user, "Password:", password)
    return True
