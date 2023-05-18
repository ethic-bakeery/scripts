from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import string

# Ask user for the number of accounts to create
num_accounts = int(input("Enter the number of Gmail accounts to create: "))

# Create a new Firefox browser instance
browser = webdriver.Firefox()

# Go to the Gmail sign-up page
browser.get('https://accounts.google.com/signup')

for i in range(num_accounts):
    # Generate a random email address
    email = ''.join(random.choices(string.ascii_lowercase, k=10))

    # Fill in the first name field
    name_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )
    name_field.send_keys(''.join(random.choices(string.ascii_letters, k=8)))

    # Fill in the last name field
    last_name_field = browser.find_element(By.ID, "lastName")

    last_name_field.send_keys(''.join(random.choices(string.ascii_letters, k=8)))

    # Fill in the username field with the generated email address
    email_field = browser.find_element(By.NAME, "Username")
    email_field.send_keys(email)

    # Fill in the password field
    password_field = browser.find_element(By.NAME, 'Passwd')
    password_field.send_keys('abdul12345')

    # Fill in the confirm password field
    confirm_password_field = browser.find_element(By.NAME,'ConfirmPasswd')
    confirm_password_field.send_keys('abdul12345')

    # Click the next button
    next_button = browser.find_element(By.ID, "accountDetailsNext")
    next_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Click the skip button
    skip_button = browser.find_element(By.ID, "sbc")
    skip_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Click the I Agree button
    agree_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "iagreebutton"))
    )
    agree_button.click()

    # Wait for the account to be created
    time.sleep(10)

    # Write the email and password to a file
    with open('gmail_accounts.txt', 'a') as f:
        f.write(f'Email: {email}\nPassword: abdul12345\n')

# Close the browser
browser.quit()

print("Done!")
