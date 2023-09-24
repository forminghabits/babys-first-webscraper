# I want money instructiond:
# 1. go to every book page n get:
# TItle
# book
# price
# availability
# UPC

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

def save_list_to_file(items, file_name):
    with open(file_name, 'w') as f:
        # Create a giant string of links where each one has a new line
        links_str = '\n'.join(items)
        f.write(links_str)


def get_links_from_pods(eles):
    links = []
    for ele in eles:
        link_ele = ele.find_element(By.TAG_NAME, "a")
        link = link_ele.get_attribute("href")
        links.append(link)
    return links


# Goes through every browse page. All 50 will contain all 1000 links to the books. you need a list of all 1000 links
all_book_links = []
for page_num in range(1, 51, 1):
    main_link = f"https://books.toscrape.com/catalogue/category/books_1/page-{page_num}.html"
    # ele class"product_pod" h3 a href
    product_pod_eles = browser.find_elements(By.CLASS_NAME, "product_pod")
    product_links = get_links_from_pods(product_pod_eles)
    all_book_links.extend(product_links)


save_list_to_file(all_book_links, "books.txt")




"""
STOP
"""
    
browser.quit()




