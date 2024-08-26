# Importing the necessary libraries
import requests
from bs4 import BeautifulSoup

# Base URL pattern with a placeholder for the page number
base_url = "https://www.buyrentkenya.com/houses-for-sale?page={}"

# function for getting content from the page in the website
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve {url}")
        return None

# function for scraping all pages in the website
def scrape_all_pages(start_page, end_page):
    for page_number in range(start_page, end_page + 1):
        url = base_url.format(page_number)
        print(f"Scraping {url}")
        soup = get_page_content(url)
        if not soup:
            break

        # Extract content from the current page
        elements = soup.find_all(class_="text-black no-underline")  # Update class name or selector as needed
        for element in elements:
            print(element.get_text(strip=True))
            #print('-' * 40)


# Define the range of pages you want to scrape
start_page = 2
end_page = 149  # Adjust based on the number of pages available

# Start scraping from the first page
scrape_all_pages(start_page, end_page)
