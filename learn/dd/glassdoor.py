import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

headers_param = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
glassdoor_url = (
    "https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm")

try:
    response = requests.get(glassdoor_url, headers=headers_param)
    response.encoding = "utf-8"
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    quit()
else:
    print(response.status_code)
    print("-"*32)

cntnt = response.content
bs = BeautifulSoup(cntnt, "html.parser")
# print(bs.title.text)

all_jobs = bs.find_all("p", {"class": "h2 m-0 entryWinner pb-std pb-md-0"})
for job in all_jobs:
    print(job.a.text)

all_data = bs.find_all("div", {"class": "col-6 col-lg-4 dataPoint"})
for data in all_data:
    print(data.text)
