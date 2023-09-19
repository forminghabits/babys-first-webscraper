#I want money instructiond:
# 1. go to every book page n get:
#TItle
#book
#price
#availability
#UPC

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

# Goes through every browse page. All 50 will contain all 1000 links to the books. you need a list of all 1000 links
all_book_links = []
for page_num in range(1,51,1):
    single_page_book_links = []
    main_link  = f"https://books.toscrape.com/catalogue/category/books_1/page-{page_num}.html"
    book_element = 

