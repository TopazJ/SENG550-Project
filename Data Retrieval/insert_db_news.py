import json
import pymongo
import sys

def insert_headers_from_json_file(year, month, start_day, end_day):
  client = pymongo.MongoClient("") #DB access address here
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

if __name__ == '__main__':
  arguments = sys.argv
  if arguments[1] == 'i':
    _, _, year, month, start_day, end_day = arguments
    month = int(month)
    start_day = int(start_day)
    end_day = int(end_day)
    insert_headers_from_json_file(year, month, start_day, end_day)
  elif arguments[1] == 'f':
    _, _, key, val = arguments
    client = pymongo.MongoClient("") #DB access address here
    db = client.seng550
    headers = db['headers']
    for article in headers.find({key: val}):
      print(article)
