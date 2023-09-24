# 1. go to every book page n get:
# TItle
# book
# price
# availability
# UPC
#pandas
import pandas as pd
# web driver is a web browser for bots
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
"""
SETUP
"""
# Set the path to the geckodriver.exe
driver_path = './geckodriver.exe'  # Update this if it's in a different location

# Create a service object using the driver path
service = Service(driver_path)
browser = webdriver.Firefox(service=service)


with open("books.txt", "r") as file:
    all_book_links = file.read().splitlines()

# print(all_book_links[:2])
book_products = []
for book_link in all_book_links:
    browser.get(book_link)
    title = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1").text
    price = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[3]").text
    availability = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[6]/td").text
    upc = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[6]/td")
    
    product_dict = {
        "title": title,
        "price": price,
        "availability": availability,
        "upc": upc,
    }
    book_products.append(product_dict)

df = pd.DataFrame(book_products)
df.to_csv("book_data.csv", index=False) 


"""
STOP
"""

browser.quit()
