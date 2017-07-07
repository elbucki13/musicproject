import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

# creates chart with dates an YT links

# billboardname = ['next-big-sound-25', 'lyricfind-us', 'lyricfind-global', 'youtube', 'spotify-rewind',
#                  'spotify-velocity', 'spotify-viral-50', 'france-songs',
#                  'german-albums', 'germany-songs', 'canadian-albums', 'hot-canada-digital-song-sales',
#                  'canadian-hot-100', 'united-kingdom-albums', 'united-kingdom-songs',
#                  'china-v-chart', 'japan-hot-100', 'world-albums', 'soundtracks', 'reggae-albums', 'new-age-albums',
#                  'jazz-songs', 'jazz-albums',
#                  'kids-albums', 'comedy-albums', 'classical-albums', 'blues-albums', 'holiday-songs',
#                  'holiday-streaming-songs', 'holiday-albums', 'holiday-season-digital-song-sales',
#                  'hot-holiday-songs', 'gospel-albums', 'gospel-streaming-songs', 'gospel-digital-song-sales',
#                  'gospel-airplay', 'gospel-songs', 'christian-albums',
#                  'christian-streaming-songs', 'christian-digital-song-sales', 'christian-airplay', 'christian-songs',
#                  'tropical-albums', 'latin-pop-albums', 'regional-mexican-albums',
#                  'latin-albums', 'tropical-songs', 'latin-pop-songs', 'regional-mexican-songs', 'latin-streaming-songs',
#                  'latin-digital-song-sales', 'latin-airplay',
#                  'latin-songs', 'dance-electronic-albums', 'hot-dance-airplay', 'dance-club-play-songs',
#                  'dance-electronic-streaming-songs', 'dance-electronic-digital-song-sales',
#                  'dance-electronic-songs', 'rhythmic-40', 'hot-adult-r-and-b-airplay', 'rap-albums', 'r-and-b-albums',
#                  'r-b-hip-hop-albums', 'rap-streaming-songs', 'rap-song', 'r-and-b-streaming-songs',
#                  'r-and-b-songs', 'r-and-b-hip-hop-streaming-songs', 'r-and-b-hip-hop-digital-song-sales',
#                  'hot-r-and-b-hip-hop-airplay', 'r-b-hip-hop-songs',
#                  'hard-rock-albums', 'hot-mainstream-rock-tracks', 'triple-a', 'alternative-albums',
#                  'alternative-songs', 'rock-albums', 'rock-streaming-songs',
#                  'rock-digital-song-sales', 'rock-airplay', 'rock-songs', 'americana-folk-albums', 'bluegrass-albums',
#                  'country-albums', 'country-streaming-songs',
#                  'country-digital-song-sales', 'country-airplay', 'country-songs', 'adult-pop-songs',
#                  'adult-contemporary', 'pop-songs', 'heatseekers-albums',
#                  'tastemaker-albums', 'catalog-albums', 'independent-albums', 'vinyl-albums', 'digital-albums',
#                  'top-album-sales', 'on-demand-streaming-songs', 'twitter-emerging-artists',
#                  'twitter-top-tracks', 'summer-songs', 'streaming-songs', 'digital-song-sales', 'radio-songs',
#                  'billboard-200', 'hot-100']
billboardname = ['hot-100', 'year-end', 'greatest-hot-100-singles', 'greatest-adult-pop-songs', 'greatest-r-b-hip-hop-songs',
                 'greatest-country-songs', 'greatest-hot-latin-songs', 'billboard-twitter-realtime', 'radio-songs',
                 'digital-song-sales', 'streaming-songs', 'summer-songs', 'twitter-top-tracks', 'on-demand-streaming-songs',
                 'social-50', 'pop-songs', 'adult-contemporary', 'adult-pop-songs', 'country-songs', 'country-airplay',
                 'country-digital-song-sales', 'country-streaming-songs', 'rock-songs', 'rock-airplay', 'rock-digital-song-sales',
                 'rock-streaming-songs', 'alternative-songs', 'triple-a', 'hot-mainstream-rock-tracks', 'r-b-hip-hop-songs',
                 'hot-r-and-b-hip-hop-airplay', 'r-and-b-hip-hop-digital-song-sales', 'r-and-b-hip-hop-streaming-songs',
                 'r-and-b-songs', 'r-and-b-streaming-songs', 'rap-song', 'rap-streaming-songs', 'hot-adult-r-and-b-airplay',
                 'rhythmic-40', 'dance-electronic-songs', 'dance-electronic-digital-song-sales', 'dance-electronic-streaming-songs',
                 'dance-club-play-songs', 'hot-dance-airplay', 'latin-songs', 'latin-airplay', 'latin-digital-song-sales',
                 'latin-streaming-songs', 'regional-mexican-songs', 'latin-pop-songs', 'tropical-songs', 'christian-songs',
                 'christian-airplay', 'christian-digital-song-sales', 'christian-streaming-songs', 'gospel-songs', 'gospel-airplay',
                 'gospel-digital-song-sales', 'gospel-streaming-songs', 'hot-holiday-songs', 'holiday-season-digital-song-sales',
                 'holiday-streaming-songs', 'holiday-songs', 'jazz-songs', 'soundtracks', 'japan-hot-100', 'china-v-chart',
                 'united-kingdom-songs', 'canadian-hot-100', 'hot-canada-digital-song-sales', 'germany-songs', 'france-songs',
                 'spotify-viral-50', 'spotify-velocity', 'spotify-rewind', 'youtube', 'lyricfind-global', 'lyricfind-us',
                 'next-big-sound-25']
for z in range(20,len(billboardname)):
    lwSongs = []
    lwLinks = []
    lwTitle = []
    currentTitle = []
    currentSongs = []
    currentLinks = []
    toCSV = []
    chartlist = billboardname[z]
    my_file = Path('' + chartlist + ' with YT Links.txt')
    if my_file.is_file():
        print('' + chartlist + ' with dates.txt exists')
        continue
    try:
        text_file = open('' + chartlist + ' with dates.txt', "r")
    except:
        continue
    lines = text_file.read().split(',,,')
    text_file.close()
    # lines = text_file.readlines()
    print(lines)
    print(len(lines))

    for x in range(len(lines)-1):
        eb = json.loads(lines[x])
        # print(eb["entries"][x]['artist'])
        for y in range(len(eb["entries"])):
            youturl = "https://www.youtube.com/results?search_query=" + eb["entries"][y]['artist'].replace("&", "") + " " + eb["entries"][y]['title'] + ""
            try:
                indx = lwSongs.index(eb["entries"][y]['title'])
                print('copy from last')
                print(youturl)
                ytLink = lwLinks[indx]
                ytTitle = lwTitle[indx]
                eb["entries"][y]['youtubeLink'] = ytLink
                eb["entries"][y]['youtubeTitle'] = ytTitle

                currentSongs.append(eb["entries"][y]['title'])
                currentLinks.append(ytLink)
                currentTitle.append(ytTitle)
            except ValueError:
                print("YTscrape")
                print(youturl)
                page = requests.get(youturl)
                soup = BeautifulSoup(page.content, 'html.parser')
                try:
                    for link in soup.find("h3", {"class": "yt-lockup-title"}):
                        try:
                            ytlink = link.get('href')
                            ytlink = str(ytlink)
                            youtlink = 'https://youtube.com' + ytlink
                            print(youtlink)
                            print(youturl)
                            ytt = link.get('title')
                            ytt = str(ytt)
                            print(ytt)
                            print(eb["entries"][y]['rank'])
                            print(eb["date"])
                            eb["entries"][y]['youtubeLink'] = youtlink
                            eb["entries"][y]['youtubeTitle'] = ytt
                            currentSongs.append(eb["entries"][y]['title'])
                            currentTitle.append(ytt)
                            currentLinks.append(youtlink)
                            break
                        except:
                            break
                except:
                    continue


        ebb = json.dumps(eb)
        print(ebb)
        toCSV.insert(0, ebb)
        del ebb
        lwSongs = currentSongs
        lwLinks = currentLinks
        lwTitle = currentTitle
        currentLinks = []
        currentTitle = []
        currentSongs = []
    thefile = open('' + chartlist + ' with YT Links.txt', 'w')
    for item in toCSV:
        thefile.write("%s,,," % item)
    text_file.close()
