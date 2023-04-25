from bs4 import BeautifulSoup
import requests
import webbrowser


def search(param: str):
    url = f"https://nontonanimeid.fun/?s={param.replace(' ', '+')}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    column_content = soup.find(class_="result")
    list_anime = []
    for index, li in enumerate(column_content.find_all("li")):
        a = li.find("a")
        href = a.get("href")
        list_anime.append(href)
        title = a.find("h2")
        print(str(index + 1), title.text)
    select_anime = int(input("Select anime : "))
    if select_anime > len(list_anime) + 1:
        exit()
    search_detail(list_anime[select_anime - 1])


def search_detail(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    column_content = soup.find(class_="episodelist")
    list_episode = []
    for index, li in enumerate(column_content.find_all("li")):
        a = li.find("a")
        href = a.get("href")
        list_episode.append(href)
        title = a.text
        print(str(index+1),title)
    select_anime = int(input("Select episode : "))
    if select_anime > len(list_episode) + 1 or select_anime <= 0:
        exit()
    else:
        webbrowser.open(list_episode[select_anime -1])