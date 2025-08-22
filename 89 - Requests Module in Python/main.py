import requests
from bs4 import BeautifulSoup

print("Script started")
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
try:
  r = requests.get(url)
  print(f"Request status code: {r.status_code}")
  r.raise_for_status()
  soup = BeautifulSoup(r.text, 'html.parser')
  print("Soup created. Printing prettified HTML (first 500 chars):")
  print(soup.prettify()[:500])
  print("\nAll h2 headings:")
  for heading in soup.find_all("h2"):
    print(heading.text)
except Exception as e:
  print(f"An error occurred: {e}")
# ...existing code...