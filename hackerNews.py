import requests
from bs4 import BeautifulSoup
# 可以print更好看的library
import pprint


# 現在是指抓到news的第一頁，如果要做別頁，可以把別頁用出來的links跟subtext加再一起，然後丟到create_custom_hn()就可以
# 第二頁的url是https://news.ycombinator.com/news?p=2，以此類推
res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titlelink")
subtext = soup.select(".subtext")


def sort_stories_by_votes(hmlist):
    # 後面key是決定要用哪個東西來sort
    # 後面reverse是反向排序
    return sorted(hmlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        # getText()可以抓到html tags中的text部分
        # item就是links[index]
        title = item.getText()
        # None是避免有link沒有href，所以給一個預設值None
        href = item.get("href", None)
        # 從subtext裡面拿到point的值
        vote = subtext[index].select(".score")
        # print(vote)
        # 有point的話才做下面，有時候一篇news會沒有point
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            # print(points)
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint((create_custom_hn(links, subtext)))


