from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def facebook_login(email, password):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the Facebook login page
    driver.get("https://www.facebook.com/")

    # Locate the email field using the id attribute
    email_field = driver.find_element_by_id("email")

    # Locate the password field using the id attribute
    password_field = driver.find_element_by_id("pass")

    # Enter the email and password
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Click the "Log In" button
    driver.find_element_by_id("u_0_b").click()

    # Wait for the user to be logged in
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "fb-timeline-cover-name")))

    # Print a success message
    print("Successfully logged in!")

    # Keep the browser open for 5 seconds before closing
    time.sleep(5)
    driver.quit()

# Replace 'your_email@example.com' and 'your_password' with your actual email and password
facebook_login('your_email@example.com', 'your_password')
