import requests
import bs4
import time

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0"}
    r = requests.get(url, headers=headers)
    time.sleep(1)
    return r

def parse_contest_list(html):
    soup = bs4.BeautifulSoup(html, features="html.parser")

    container = soup.find("div", attrs= {"class":"active_contests"})
    cards = container.find_all("div", attrs= {"data-analytics":"ContestCardSignupLink"})

    for card in cards:
        name = card.find("h4").get_text(strip=True)
        time_info = card.find("div", class_="contest-item__time").get_text(strip=True)
        link = card.find("a")
        url = "https://www.hackerrank.com" + link["href"] if link else None

        print(name, time_info, url)

res = fetch_page("https://www.hackerrank.com/contests")
parse_contest_list(res.text)