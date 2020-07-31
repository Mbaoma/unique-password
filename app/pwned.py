import hashlib
import requests

def check_pwned(password):
    password_hash = hashlib.sha1(password.encode()).hexdigest()
    head, tail = password_hash[:5], password_hash[5:]

    try:
        api_url = "https://api.pwnedpasswords.com/range/" + head
        r = requests.get(api_url)
        if r.status_code != 200:
            raise Exception
    except:
        return {
            "success": False
        }

    response = {
        "success": True,
        "count": 0
    }
    for i in r.text.lower().split("\n"):
        j = i.split(":")
        if j[0] == tail:
            response["count"] = int(j[1])
            break

    return response
