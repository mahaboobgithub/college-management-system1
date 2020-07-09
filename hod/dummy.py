
import requests
from bs4 import BeautifulSoup

response = requests.get("https://mylocation.org/")

bs = BeautifulSoup(response.text,"html.parser")

res = bs.find_all("td")

print(res[10].text)
print(res[11].text)

