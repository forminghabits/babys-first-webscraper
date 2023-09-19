"""
Docstrings are meant to be a large comment, 
when they at the top of the file they are describing everything about this file

Baby's first webscraper task:

1. Go to homepage CHECK
2. Find the navigation element 
3. Find all the urls inside the navigation

"""

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

home_page = 'http://quotes.toscrape.com/'


browser.get(home_page)
sleep(3)

def parse_from_quote_elements(quote_elements):
    quotes_of_page = [] 
    
        #iterating over each quote_element from quote_elements list to extract text
    for quote_element in quote_elements: 
        # Text
        quote_text_element = quote_element.find_element(By.CLASS_NAME, 'text')
        quote_text = quote_text_element.text
        # Author
        quote_author_element = quote_element.find_element(By.CLASS_NAME, 'author')
        quote_author = quote_author_element.text
        # Tags
        quote_tags_element = quote_element.find_element(By.CLASS_NAME, 'keywords')
        quote_tags = quote_tags_element.get_attribute('content')
        # Make a dictionary with text, author, and tags. 
        # Each key:value pair should be seperated by a comma
        quote_dict = {
            'text': quote_text,
            'author': quote_author,
            'tags': quote_tags.split(',')
        }
        quotes_of_page.append(quote_dict)

    return quotes_of_page
"""
STEP 2

Target: Navigation box
Element Type: Div
Classes: col-md-4 and tags-box

More than one element can have the same class
We want to find a specific element but cant be sure the class will 
do that

So we can check 
We have two classes in the target, We can ctrl f in the inspect
element screen, to make sure the one we use is unique to the nav bar

It looks like col-md-4 is not unique, but tags-box is, so we use that
"""

# Get the navigation element as a whole
navigation_box = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]")

# Get all the links of the navigation box, notice are use of find_element(s)
nav_elements = navigation_box.find_elements(By.CLASS_NAME, "tag")

# Get our list rady to put the links in 
all_links = []

for nav_element in nav_elements:
    # Make variables for link text and link url
    nav_link = nav_element.get_attribute('href')
    all_links.append(nav_link)

# Go to all webpages
all_quotes = []
for link in all_links:
    sleep(.5)
    browser.get(link) # click link
    quote_box = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[1]") #finding quote box element
    quote_elements = quote_box.find_elements(By.CLASS_NAME, "quote") #finding quote elements in the quote box add
    quotes_of_page = parse_from_quote_elements(quote_elements)
    all_quotes.extend(quotes_of_page)

for quote in all_quotes:
    print(quote)
    sleep(2)


"""
STOP
"""
sleep(10)
browser.quit()


