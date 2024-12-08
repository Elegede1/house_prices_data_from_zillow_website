from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# get the page source using requests
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

price_span_tags = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")

# Loop through each tag and extract the price and put it in a list
prices = [tag.text.split("+")[0].split("/")[0].strip() for tag in price_span_tags]

# # Print the list of prices
# print(prices)


# get the links to the properties hrefs
property_links = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
# get href from the first property link

# loop through the property links and get the hrefs
property_hrefs = [link.get("href") for link in property_links]


# # print the list of property hrefs
# print(property_hrefs)



# loop through the property links and get the addresses
property_addresses = [link.text.strip().replace("|", "") for link in property_links]
# # print the list of property addresses
# print(property_addresses)


# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up Chrome driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfW50gv11slalquzY8sX35G0Kv93QWmvD6nd6xbwZ-Gt_4v_A/viewform?usp=dialog")


# Wait for the page to load
wait = WebDriverWait(driver, 10)


# loop through the property addresses, prices, and links and fill in the form
for i in range(len(property_addresses)):
    # get the input fields
    address_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))  # This input is for the addressprice
    price_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))  # This input is for the price
    link_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))  # This input is for the link
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))  # This button is for the submit button

    # fill in the input fields
    address_input.send_keys(property_addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(property_hrefs[i])
    submit_button.click()

    # wait for the next page to load
    submit_another_response = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    submit_another_response.click()