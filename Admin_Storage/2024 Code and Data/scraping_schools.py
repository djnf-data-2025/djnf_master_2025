import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://nil.store/'

# Fetch the webpage content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific div containing the school names and URLs
schools_nav = soup.find('div', class_='mega_menu_main', id='schools-nav')

# Check if the element is found
if schools_nav:
    # Find all the list items within this div
    school_list_items = schools_nav.find_all('li', class_='only_link')

    # Extract the school names and URLs from the list items
    schools = []
    for item in school_list_items:
        link = item.find('a')
        if link:
            school_name = link.text.strip()
            school_url = link['href'].strip()
            schools.append({'name': school_name, 'url': school_url})

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(schools)

    # Print the DataFrame
    print(df)
else:
    print("The specified div element with class 'mega_menu_main' and id 'schools-nav' was not found.")
