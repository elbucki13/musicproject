from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.billboard.com/charts/")
                    # print(page)
soup = BeautifulSoup(page.content, 'html.parser')
prevLink = soup.findAll('a',{})
list_of_charts = []
album_charts = []
song_charts = []
artist_charts = []
for a in soup.find_all('a', href=True):
    tester = str(a['href'])


    if "/charts/" in tester:
        tester = tester.split("/charts/", 1)[1]
        if tester in list_of_charts or "/" in tester:
            continue
        else:
            if "album" in tester or "billboard-200" in tester:
                album_charts.append(tester)
            elif "artist" in tester:
                artist_charts.append(tester)
            else:
                song_charts.append(tester)
            list_of_charts.append(tester)
            print(tester)

print(list_of_charts)
print(artist_charts)
print(album_charts)
print(song_charts)
print('There are ' + str(len(song_charts)) + ' charts with songs, ' + str(len(album_charts)) + ' with albums, and ' + str(len(artist_charts)) +
      ' with artists.')

# print(testing)