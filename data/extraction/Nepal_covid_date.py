import os
import requests
import json
import pandas as pd
from datetime import date

retval = os.getcwd()
os.chdir( "/".join(retval.split("/")[:-1]))
retval = os.getcwd()

url1 = "https://pomber.github.io/covid19/timeseries.json"

data = requests.get(url1)
json_data = json.loads(json.dumps(data.json()))
countries = json_data.keys()
print(countries)

#To save the whole data
# df = pd.DataFrame(columns=["country","date","confirmed","deaths","recovered"])
# for country in list(countries):
#     for i in json_data[country]:
#         df = df.append({"country":country,"date":i["date"],"confirmed":i["confirmed"],"deaths":i["deaths"],"recovered":i["recovered"]},ignore_index=True)


# to fetch only Nepal's Data
country = "Nepal"
df = pd.DataFrame(columns=["country","date","confirmed","deaths","recovered"])
for i in json_data[country]:
    df = df.append({"country":country,"date":i["date"],"confirmed":i["confirmed"],"deaths":i["deaths"],"recovered":i["recovered"]},ignore_index=True)

df = df.drop(["country"], axis = 1)

today = date.today()
df.to_csv(retval+"/nepal_covid-date(22Jan-"+str(today)+").csv",index=False)

