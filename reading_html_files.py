# Reading the HTML file
import requests
from bs4 import BeautifulSoup

# Fetch the html file
url = 'http://tutorialspoint.com/python/python_overview.htm'
response = requests.get(url)
html_doc = response.text

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print(strhtm[:225])

print("\n")

# Extracting Tag Value
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

print("\n")
print("\n")
# Extracting All Tags
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all('b'):
    print(x.string)


