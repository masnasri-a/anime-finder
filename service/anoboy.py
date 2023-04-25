from bs4 import BeautifulSoup
import requests
import webbrowser

def search_anoboy(anime_name:str, pages = 1):
    page_num = pages
    page = requests.get(f"https://anoboy.monster/page/{page_num}/?s={anime_name.replace(' ','+')}")
    soup = BeautifulSoup(page.content, "html.parser")
    column_content = soup.find(class_="column-content")
    if column_content:
        detail_data = column_content.find_all("a")
        list_anime = []
        for index, detail in enumerate(detail_data):
            try:
                list_anime.append(detail.get("href"))
                title = detail.find("h3")
                print(str(index+1),title.text)
            except:
                break
        select_anime = int(input("Select anime [0 = more]: "))
        if select_anime == 0:
            search_anoboy(anime_name, page_num+1)
        else:
            webbrowser.open(list_anime[select_anime-1])
    else:
        print("Anime Not Found")
