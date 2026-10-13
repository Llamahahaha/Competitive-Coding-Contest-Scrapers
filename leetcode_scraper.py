import requests
import datetime

url = 'https://leetcode.com/graphql/' 

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0',
    'content-type': 'application/json',
    'Referer': 'https://leetcode.com/contest/'
}

query = {
    "query": """
        query contestV2UpcomingContests {
            contestV2UpcomingContests {
                titleSlug
                title
                titleCn
                startTime
                duration
                cardImg
                cardImgApp
                }
            }
        """,
    "variables":{},
    "operationName":"contestV2UpcomingContests"
}

response = requests.post(url, json=query, headers=headers)

for value in response.json()['data']['contestV2UpcomingContests']:
    start = datetime.datetime.fromtimestamp(value['startTime'])
    hours, remainder = divmod(value['duration'], 3600)
    minutes = remainder//60
    print(value['title'], ":", start.strftime("%Y-%m-%d %H:%M"), ":", f"{hours}h {minutes}m")

