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
driver_path = './geckodriver'  # Update this if it's in a different location

# Create a service object using the driver path
service = Service(driver_path)

browser = webdriver.Firefox(service=service)
"""
END SETUP
"""

"""
LINKS
"""
home_page = 'http://quotes.toscrape.com/'
"""
END LINKS
"""

"""
STEP 1
"""
# Step 1
browser.get(home_page)
sleep(3)
"""
END STEP1
"""

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


def parse_quotes_from_quote_elements(quote_elements):
    quotes_of_page = [] 
        #iterating over each quote_element from quote_elements list to extract text
    for quote_element in quote_elements: 
        quote_text = quote_element.text
        quotes_of_page.append(quote_text)

    return quotes_of_page


# Get the navigation element as a whole
navigation_box = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]")

# Get all the links of the navigation box, notice are use of find_element(s)
nav_elements = navigation_box.find_elements(By.CLASS_NAME, "tag")

# Get our list rady to put the links in 
all_links = []

for nav_element in nav_elements:
    # Make variables for link text and link url
    nav_text = nav_element.text
    nav_link = nav_element.get_attribute('href')
    all_links.append(nav_link)
print(f"{len(all_links)=}")
# Go to all webpages
all_quotes = []
for link in all_links:
    sleep(.5)
    browser.get(link) # click link
    quote_box = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[1]") #finding quote box element
    quote_elements = quote_box.find_elements(By.CLASS_NAME, "text") #finding quote elements in the quote box add
    quotes_of_page = parse_quotes_from_quote_elements(quote_elements)
    all_quotes = (all_quotes + quotes_of_page)





# PRINT QUOTES SLOWLY
print(f"{len(all_quotes)=}")


for quote in all_quotes:
    print(quote)
    sleep(.5)

print(f'{5 + 6} {5+6=}')
    # Quotes div xpath: /html/body/div/div[2]/div[1]
    # Get quotes div ele
    # Find all quotes within it
    # for each link, store the text to a list



"""
END STEP 2
"""


"""
STOP
"""
sleep(10)
browser.quit()


