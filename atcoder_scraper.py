#import requests
#import time
#data = requests.get("https://kenkoooo.com/atcoder/resources/contests.json").json()
#for contest in data:
#    if(int(contest["start_epoch_second"])> int(time.time())):
#        print(contest["title"])

import requests
import bs4
import time
import os #operating sytem level funcitonality
import csv
from datetime import datetime

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0"
    }
    res = requests.get(url, headers=headers)
    time.sleep(1)
    return res

def parse_contest_list(html):
    soup = bs4.BeautifulSoup(html, features="html.parser")

    container = soup.select_one('div#contest-table-upcoming') #returns Tag
    table = container.select_one('tbody')
    rows = table.select('tr') #returns resultSet of Tags

    lst = []
    for row in rows:
        cells = row.select('td')
        if len(cells) < 2:
            continue
        span1 = cells[0].select_one('a')
        span2 = cells[1].select_one('span')
        keys = ["time", "name"]
        dict1 = dict.fromkeys(keys)
        if span1:
            time_tag = cells[0].select_one('a')
            dt = datetime.strptime(time_tag.text, "%Y-%m-%d %H:%M:%S%z")
            #print(dt.strftime("%Y-%m-%d %H:%M"))
            dict1["time"]= dt.strftime("%Y-%m-%d %H:%M")
        if span2:
            link = cells[1].select_one('a')
            #print(link.text)
            dict1["name"]= link.text
        
        if span1 and span2:
            lst.append(dict1)
    return lst

# def save_to_csv(data, path):
#     outputFile = open(path, 'w', newline='')
#     outputWriter = csv.writer(outputFile)
#     outputWriter.writerow(['Time', 'Contest'])
#     for x in data:
#         outputWriter.writerow([x["time"], x["name"]])    

if __name__ == "__main__": 
    url = "https://atcoder.jp/contests/"
    response = fetch_page(url)

    os.makedirs("data/raw_html/", exist_ok=True)

    with open("data/raw_html/contests.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    html = open("data/raw_html/contests.html", "r")
    # save_to_csv(parse_contest_list(html), 'output.csv')