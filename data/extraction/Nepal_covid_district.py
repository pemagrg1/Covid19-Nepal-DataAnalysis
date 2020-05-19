"""
Scraping code Reff: https://www.kaggle.com/milan400/nepal-coronavirus-real-time-data-analysis. You can also check his Analysis which is pretty cool :)
"""

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

retval = os.getcwd()
os.chdir( "/".join(retval.split("/")[:-1]))
retval = os.getcwd()

URL = "https://coronanepal.live/"
page = requests.get(url=URL)
soup = BeautifulSoup(page.text)

all_links = soup.find_all("a")
for link in all_links:
    pass

all_tables = soup.find('table')

A = []
B = []
C = []
D = []
E = []
F = []

for row in all_tables.findAll("tr"):
    cells = row.findAll('td')

    # Only extract table body
    if (len(cells) == 6):
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))

df = pd.DataFrame()

df['district_nepali'] = A
df['district'] = B
df['confirmed'] = C
df['deaths'] = E
df['recovered'] = F

df = df.astype({'district_nepali': str, 'district': str, 'confirmed': int, 'deaths': int, 'recovered': int})
df_nepal = df.astype({'district_nepali': str, 'district': str, 'confirmed': int, 'deaths': int, 'recovered': int})

today = date.today()
df_nepal.to_csv(retval+"/districtwise_nepalCovidData(22Jan-"+str(today)+").csv",index=False)
