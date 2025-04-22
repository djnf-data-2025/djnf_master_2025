import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://nil.store/pages/boise-state-sports'

# Fetch the content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to store the names and URLs
    names = []
    urls = []

    # Find the specific section that contains athlete names, excluding header-drawer
    athlete_section = soup.select('nav > ul > li:nth-of-type(3) > div > div > div > div:nth-of-type(3) > ul')

    if athlete_section:
        # Find all 'li' elements within this section
        li_elements = athlete_section[0].find_all('li', class_='only_link')
        
        for li in li_elements:
            # Find the 'a' tag within each 'li' element
            a_tag = li.find('a', class_='color-text')
            if a_tag:
                # Get the text inside the 'a' tag
                name = a_tag.text.strip()
                # Get the URL inside the 'a' tag
                url = 'https://nil.store' + a_tag['href']
                
                # Add the name and URL to the lists
                names.append(name)
                urls.append(url)

    # Create a DataFrame
    df = pd.DataFrame({'Name': names, 'URL': urls})

    # Print the DataFrame
    print(df)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
