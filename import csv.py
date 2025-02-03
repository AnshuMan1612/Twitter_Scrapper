import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the user URL and username
user_url = "https://twitter.com/GTNUK1"  # Replace with the desired username
user_name = "GTNUK1"  # Replace with the desired username

# Create a new Chrome webdriver instance
driver = webdriver.Chrome()

# Navigate to the user page
driver.get(user_url)

# Wait for the page to load
wait = WebDriverWait(driver, 20)  # Increased wait time

# Scrape the bio, location, website, and join date
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract the bio
try:
    bio_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='UserDescription']")))
    bio = bio_elements[0].text.strip() if bio_elements else ""
except Exception as e:
    bio = ""
    print("Error fetching bio: {}".format(e))  # Error handling

# Extract the location
try:
    location_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='UserLocation']")))
    location = location_elements[0].text.strip() if location_elements else ""
except Exception as e:
    location = ""
    print("Error fetching location: {}".format(e))  # Error handling

# Extract the website
try:
    website_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='UserUrl']")))
    website = website_elements[0].text.strip() if website_elements else ""
except Exception as e:
    website = ""
    print("Error fetching website: {}".format(e))  # Error handling

# Extract the join date
try:
    join_date_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='UserJoinDate']")))
    join_date = join_date_elements[0].text.strip() if join_date_elements else ""
except Exception as e:
    join_date = ""
    print("Error fetching join date: {}".format(e))  # Error handling

# Define the CSV file path
csv_file = "twitter_data.csv"

# Create the CSV file if it does not exist
import os
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Name", "Bio", "Location", "Website", "Join Date"])
    print("CSV file created: {}".format(csv_file))  # Debugging statement
else:
    print("CSV file already exists: {}".format(csv_file))  # Debugging statement

# Write the data to the CSV file
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([user_name, bio, location, website, join_date])
