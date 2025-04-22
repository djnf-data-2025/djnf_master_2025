import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://nil.store/collections/bsu-aidan-palmer"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product name elements
product_elements = soup.select('div h3 a')

# Find all price elements
price_elements = soup.select('span.price-item.price-item--regular')

# Extract and pair the text of each product name and price
products = []
for product, price in zip(product_elements, price_elements):
    product_name = product.get_text().strip()
    product_price = price.get_text().strip()
    products.append((product_name, product_price))

# Create a DataFrame from the extracted data
df = pd.DataFrame(products, columns=['Product Name', 'Price'])

# Print the DataFrame
print(df)
