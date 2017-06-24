

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
# from get_billboard_data import youtube_search
def youtube_search(artist, title):
    import requests
    from bs4 import BeautifulSoup
    youtubeurl = "https://www.youtube.com/results?search_query=" + artist.replace("&", "") + " " + \
              title + ""

    page = requests.get(youtubeurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        for link in soup.find("h3", {"class": "yt-lockup-title"}):
            try:
                ytlink = link.get('href')
                ytlink = str(ytlink)
                youtubelink = 'https://youtube.com' + ytlink
                ytt = link.get('title')
                ytt = str(ytt)
                return {'returned_link': youtubelink, 'returned_ytt': ytt}
            except:
                return ''
    except:
        return ''
from get_billboard_data import spotify_search
import pprint


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
    lwSongs,lwLinks,lwTitle,currentTitle,currentSongs,currentLinks = ([] for i in range(6))
    toCSV = []
    chartlist = billboardname[z]
    my_file = Path('' + chartlist + ' with dates.txt')
    if my_file.is_file():
        print('' + chartlist + ' with dates.txt exists')
    try:
        text_file = open('' + chartlist + ' with dates.txt', "r")
        print('' + chartlist + 'dates')
    except:
        continue
    lines = text_file.read()
    outer_dict = json.loads(lines)
    text_file.close()
    # print(eb[chartlist][0])
    for x in range(len(outer_dict[chartlist])):
        type(outer_dict[chartlist][x])
        eb = json.loads(outer_dict[chartlist][x])
        for y in range(len(eb['entries'])):
            print(eb['entries'][y]['title'])
            try:
                indx = lwSongs.index(eb['entries'][y]['title'])
                print("{} is already found using old link.".format(eb['entries'][y]['title']))
                ytLink = lwLinks[indx]
                ytTitle = lwTitle[indx]
                eb['entries'][y]['youtubeLink'] = ytLink
                eb['entries'][y]['youtubeTitle'] = ytTitle

                currentSongs.append(eb['entries'][y]['title'])
                currentLinks.append(ytLink)
                currentTitle.append(ytTitle)
            except ValueError:
                print("YTscrape for {} by {}".format(eb["entries"][y]['title'],eb["entries"][y]['artist']))
                func_return = youtube_search(eb["entries"][y]['artist'],eb["entries"][y]['title'])
                eb["entries"][y]['youtubeLink'] = func_return['returned_link']
                eb["entries"][y]['youtubeTitle'] = func_return['returned_ytt']
                print('Found {} for {}.'.format(func_return['returned_link'],func_return['returned_ytt']))
                currentSongs.append(eb["entries"][y]['title'])
                currentTitle.append(func_return['returned_ytt'])
                currentLinks.append(func_return['returned_link'])
            SPO_ID = eb["entries"][y]['spotifyID']

            if not SPO_ID:
                try:
                    SPOO = spotify_search(eb["entries"][y]['artist'], eb["entries"][y]['title'])
                    eb["entries"][y]['spotifyID'] = SPOO
                    eb["entries"][y]['spotifyID'] = 'https://embed.spotify.com/?uri=spotify:track:' + SPOO
                    print('{} is the code for {} by {}'.format(SPOO,eb["entries"][y]['title'],eb['entries'][y]['artist']))
                except:
                    print('Cant find {} by {}'.format(eb["entries"][y]['title'],eb['entries'][y]['artist']))
                    eb["entries"][y]['spotifyID'] = 'No Spotify ID Found'
                    eb["entries"][y]['spotifyLink'] = 'No Spotify Link Found'
                    print(json.dumps(eb["entries"][y], indent=4, sort_keys=True))
        ebb = json.dumps(eb)
        print(ebb)
        toCSV.append(ebb)
        del ebb
        lwSongs = currentSongs
        lwLinks = currentLinks
        lwTitle = currentTitle
        currentLinks = []
        currentTitle = []
        currentSongs = []
    new_dict = dict()
    new_dict[chartlist] = toCSV
    ebb = json.dumps(new_dict)
    print(ebb)
    thefile = open('' + chartlist + ' with YT Links.txt', 'w')
    thefile.write(ebb)
    thefile.close()










