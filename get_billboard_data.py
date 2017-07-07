
def get_billboard_data(chartlist):
    # creates billboard chart csv with given chart or if none given empty string

    if chartlist is '':
        print('None')

    print(chartlist + ' is chartlist')

    import billboard_new
    import csv
    import json
    from pathlib import Path

    # creates chart with dates csv


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

    miss_count = 0
    toCSV = []

    if chartlist is '':
        for b in range(0,len(billboardname)):

            chartlist = billboardname[b]
            my_file = Path('' + chartlist + ' with dates.json')
            if my_file.is_file():
                print('' + chartlist + ' with dates.json exists')
                continue
            try:
                print('Running ' + billboardname[b] + ' charts')
                chart = billboard_new.ChartData(chartlist)
                print(chart)
                toCSV = []
                chart.previousDate = chart.date

                with open('dates.csv', 'r') as f:
                    reader = csv.reader(f)
                    dates = list(reader)
                for i in range(0,len(dates)):
                    try:
                        helper = str(dates[i])
                        helper = helper[2:12]
                        print(helper + ' is helper for ' + chartlist)
                        chart = billboard_new.ChartData(chartlist, helper, quantize=False)
                    except Exception as ex:
                        print(ex)
                        miss_count = miss_count + 1
                        if miss_count < 100:
                            print('Charts cant load ' + chartlist + str(dates[i]))
                            continue
                        else:
                            break
                    if len(chart.entries) > 5:
                        eli2 = chart.to_JSON()
                        toCSV.insert(0,eli2)
                        del eli2
                        miss_count = 0
                    else:
                        miss_count = miss_count + 1
                        if miss_count > 100:
                            break
                        print('no entires')
                miss_count = 0




                print('writing files for ' + billboardname[b])

                new_dict = dict()
                new_dict[chartlist] = toCSV
                ebb = json.dumps(new_dict)
                print(ebb)
                thefile = open('' + chartlist + ' with dates.txt', 'w')
                thefile.write(ebb)
                # thefile.write("]")
                thefile.close()

            except Exception as e:
                print('last')
                print(e)

    else:

        my_file = Path('' + chartlist + ' with dates.txt')
        if my_file.is_file():
            print('' + chartlist + ' with dates.txt exists')
            return
        try:
            print('Running ' + chartlist + ' charts')
            chart = billboard_new.ChartData(chartlist)
            print(chart)
            toCSV = []
            chart.previousDate = chart.date

            with open('dates.csv', 'r') as f:
                reader = csv.reader(f)
                dates = list(reader)
            for i in range(0, len(dates)):
                try:
                    helper = str(dates[i])
                    helper = helper[2:12]
                    print(helper + ' is helper for ' + chartlist)
                    chart = billboard_new.ChartData(chartlist, helper, quantize=False)
                except Exception as ex:
                    print(ex)
                    miss_count = miss_count + 1
                    if miss_count < 100:
                        print('Charts cant load ' + chartlist + str(dates[i]))
                        continue
                    else:
                        break
                if len(chart.entries) > 5:
                    eli2 = chart.to_JSON()
                    toCSV.insert(0,eli2)
                    del eli2
                    miss_count = 0
                else:
                    miss_count = miss_count + 1
                    if miss_count > 100:
                        break
                    print('no entires')
            miss_count = 0

            print('writing files for ' + chartlist)
            new_dict = dict()
            new_dict[chartlist] = toCSV
            ebb = json.dumps(new_dict)
            print(ebb)
            thefile = open('' + chartlist + ' with dates.txt', 'w')
            thefile.write(ebb)
            # thefile.write("]")
            thefile.close()

        except Exception as e:
            print('last')
            print(e)

def spotify_search(artist,title):
    import spotipy
    import spotipy.util as util
    scope = 'user-library-read'
    username = 'Eli Brantingham'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    artist = artist.replace("&", "")
    artist = artist.split("Featuring", 1)[0]
    #artist = artist.replace(" ","%20")
    # title = title.replace(" ","%20")
    search_str = "artist:{} track:{}".format(artist, title)
    result = sp.search(search_str,type='track',limit=5)
    try:
        SPOO = result["tracks"]['items'][0]['id']
        print(search_str + ' ' + SPOO)
        return SPOO
    except:
        print("Can't find " + search_str)
        print(result)
        return ""

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

if __name__ == "__main__":
    # get_billboard_data('')c
    # spotify_search('the who who are you')
    #print(youtube_search('blink-182','roller coaster'))
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
    for x in range(00,150):
        get_billboard_data(billboardname[x])



