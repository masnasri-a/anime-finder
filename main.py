from service import anoboy, nontonanimeid

if __name__ == '__main__':
    param = input("Search your anime : ")
    # param = "isekai de cheat"
    print("Select Platform")
    platforms = ["Anoboy","NontonAnimeId"]
    print("========================== Anoboy ==========================")
    for index, platform in enumerate(platforms):
        print(str(index+1), platform)
    select_platform = int(input("Select Platform : "))
    if select_platform == 1:
        anoboy.search_anoboy(param)
    elif select_platform == 2:
        nontonanimeid.search(param)