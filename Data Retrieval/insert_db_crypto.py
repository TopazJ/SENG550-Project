import calendar
import json
import numpy as np
import pandas as pd
import pymongo
import sys

month_abbr_to_num = {month: index for index, month in enumerate(calendar.month_abbr) if month}
DB_access_address = ""  # Paste DB access address here

def insert_headers_from_json_file(year, month, start_day, end_day):
  client = pymongo.MongoClient(DB_access_address) 
  db = client.seng550
  headers = db['headers']
  month_s = month if month >= 10 else f"0{month}"

  for day in range(start_day, end_day+1):
    day_s = day if day >= 10 else f"0{day}"
    filename = f"headlines_{year}-{month_s}-{day_s}.json"
    with open(filename) as f:
      articles = json.load(f)['articles']
      for article in articles:
        d = {'headline': article['title'], 'date': article['publishedAt'].split('T')[0]}
        result = headers.insert_one(d)
        print(result.inserted_id)

def convert_crypto_date_to_iso_8601(date):
  # Oct-23-2021 -> 2021-10-23
  month, day, year = date.split('-')
  month = month_abbr_to_num[month]
  month = str(month) if month >= 10 else f'0{month}'
  return "-".join([year, month, day])
  
  

if __name__ == '__main__':
  arguments = sys.argv
  if arguments[1] == 'h':
    if arguments[2] == 'i':
      _, _, _, year, month, start_day, end_day = arguments
      month = int(month)
      start_day = int(start_day)
      end_day = int(end_day)
      insert_headers_from_json_file(year, month, start_day, end_day)
    elif arguments[2] == 'f':
      _, _, _, key, val = arguments
      client = pymongo.MongoClient(DB_access_address)
      db = client.seng550
      headers = db['headers']
      for article in headers.find({key: val}):
        print(article)
  elif arguments[1] == 'c':
    client = pymongo.MongoClient(DB_access_address)
    db = client.seng550
    crypto = db['crypto']
    if arguments[2] == 'i':
      crypto_prices_df = pd.read_csv(arguments[3], dtype={'Open': np.float64, 'Close': np.float64}).drop(['High', 'Low', 'Volume', 'Market Cap'], axis=1)
      crypto_prices_df['Date'] = crypto_prices_df['Date'].apply(convert_crypto_date_to_iso_8601)
      for row in crypto_prices_df.itertuples():
        idx, date, open_, close = row
        if idx > 300:
          break;
        d = {'date':date, 'open':open_, 'close':close}
        result = crypto.insert_one(d)
        print(result.inserted_id)
    elif arguments[2] == 'f':
      _, _, _, key, val = arguments
      for prices in crypto.find({key: val}):
        print(prices)
