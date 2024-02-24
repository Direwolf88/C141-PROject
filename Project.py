from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

list_of_brown_dwarfs = []

browser.get(START_URL)


soup = BeautifulSoup(browser.page_source, "html.parser")

star_table = soup.find("table")
temb_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temb_list.append(row)

star_names = []
distance = []
mass = []
radius = []
lum = []

for i in range(1, len(temb_list)):
    star_names.append(temb_list[i][1])
    distance.append(temb_list[i][3])
    mass.append(temb_list[i][5])
    radius.append(temb_list[i][6])
    lum.append(temb_list[i][7])

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['star_name','distance','mass','radius','luminosity'])
df2.to_csv("dwarf.csv")