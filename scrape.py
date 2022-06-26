import requests
from bs4 import BeautifulSoup

# 用來取得網頁資訊
res = requests.get("https://news.ycombinator.com/news")

# 取得的東西會是string，需要beautifulSoup的parse去轉成可以實際使用的soup object
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# print("---------------------")
# soup object就可以做各種操作
# print(soup.head)
# 找所有div tag，find_all會存成list
# print(soup.find_all("div"))
# 找對應的id
# print(soup.find(id="score_31880394"))
# print("---------------------")

# css selector
# 網站結構的關係，第一個link就會對應到第一個vote
# 找到每一個titlelink，結果會是一個list
links = soup.select(".titlelink")
votes = soup.select(".score")
print(links[0])
# 用get去取得votes[0]裡面id的值
print(votes[0])
print(votes[0].getText())

