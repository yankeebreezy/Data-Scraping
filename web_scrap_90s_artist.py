# web scrapping top 100 artists of the 90's from url https://top40weekly.com/top-100-artists-of-the-90s/

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

artist_list = []

content = requests.get("https://top40weekly.com/top-100-artists-of-the-90s/")

soup = BeautifulSoup(content.text, 'html.parser')
for a in soup.findAll('a', href=True, attrs={'rel':'noopener nofollow noreferrer'}):
    artist_list.append(a.text)
    
artistDf = pd.DataFrame({'Artist': artist_list})
artistDf.to_csv('artists.csv', index = False, encoding = 'utf-8')