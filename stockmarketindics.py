# Import library
from datetime import timedelta
import datetime
import time
import pandas as pd

# Dictionary to hold G20 countries and their respective stock indics
g20_indics = {
    'Argentina':'^MERV', 
    'Australia':'^AXJO', 
    'Brazil':'^BVSP', 
    'Canada':'^GSPTSE', 
    'China':'000001.SS', 
    'France':'^FCHI', 
    'Germany':'^GDAXI', 
    'India':'^BSESN', 
    'Indonesia':'^JKSE', 
    'Italy':'FTSEMIB.MI', 
    'Japan':'^N225', 
    'South Korea':'^KS11', 
    'Mexico':'^MXX', 
    'Russia':'IMOEX.ME', 
    'Saudi Arabia':'^TASI.SR', 
    'South Africa':'^JN0U.JO', 
    'Turkey':'XU100.IS', 
    'UK':'^FTSE', 
    'US':'^NYA',
    'EU':'^N100'
}

# yahoo finance url to download historical data
yahoo_fin_url = 'https://query1.finance.yahoo.com/v7/finance/download/indics?period1=startdate&period2=enddate&interval=1d&events=history'

# Today's and Previous year date & time
today = datetime.datetime.now()
prevYearDateTime = today - timedelta(days=366)
pattern = '%Y-%m-%d %H:%M:%S'
startDate = prevYearDateTime.strftime(pattern)
endDate = today.strftime(pattern)
# Convert to epoch time
startEpochTime = int(time.mktime(time.strptime(startDate,pattern)))
endEpochTime = int(time.mktime(time.strptime(endDate,pattern)))
stockMarketDf = pd.DataFrame()

# Iterate indics dict to download the data
for key,value in g20_indics.items():
    # Create a url with indics and time
    url = yahoo_fin_url.replace('indics',value).replace('startdate', str(startEpochTime)).replace('enddate', str(endEpochTime))
    # Download the individual country stock data
    countryStockData = pd.read_csv(url)
    # Create column country and indics
    countryStockData['Country'] = key
    countryStockData['Indics'] = value
    # Add data to the dataframe
    stockMarketDf = stockMarketDf.append(countryStockData)
    
# Print data
print(stockMarketDf.head())
