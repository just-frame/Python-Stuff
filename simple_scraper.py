import requests
from bs4 import BeautifulSoup

# Make a request make sure to enter the site you want to scrape in the url
page = requests.get("https://scrape me dot com")
soup = BeautifulSoup(page.content, 'html.parser') # get the page content with the html parser

# response = requests.get(page) # get the response
# Extract title of page
# page_title = soup.find('title')
page_title = soup.title

# Extract body of page
# page_body = soup.find('body')
page_body = soup.body

# Extract head of page 
# page_head = soup.find('head')
page_head = soup.head

# print the result you can remove the variable you don't want to print by deleting it from the print statement
print(page_title, page_body, page_head)