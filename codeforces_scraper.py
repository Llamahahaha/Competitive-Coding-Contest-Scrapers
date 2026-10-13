import requests
data = requests.get("https://codeforces.com/api/contest.list").json()
contests = data["result"]
for contest in contests:
    if(contest['phase']=='BEFORE'):
        print(contest["name"])