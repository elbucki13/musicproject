from bs4 import BeautifulSoup
import urllib

import requests

# Old version using 5 csv files to save billboard data

year = ['1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
day = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
billboardname = ['next-big-sound-25','lyricfind-us','lyricfind-global','youtube','spotify-rewind','spotify-velocity','spotify-viral-50','france-songs',
                 'german-albums','germany-songs','canadian-albums','hot-canada-digital-song-sales','canadian-hot-100','united-kingdom-albums','united-kingdom-songs',
                 'china-v-chart','japan-hot-100','world-albums','soundtracks','reggae-albums','new-age-albums','jazz-songs','jazz-albums',
                 'kids-albums','comedy-albums','classical-albums','blues-albums','holiday-songs','holiday-streaming-songs','holiday-albums','holiday-season-digital-song-sales',
                 'hot-holiday-songs','gospel-albums','gospel-streaming-songs','gospel-digital-song-sales','gospel-airplay','gospel-songs','christian-albums',
                 'christian-streaming-songs','christian-digital-song-sales','christian-airplay','christian-songs','tropical-albums','latin-pop-albums','regional-mexican-albums',
                 'latin-albums','tropical-songs','latin-pop-songs','regional-mexican-songs','latin-streaming-songs','latin-digital-song-sales','latin-airplay',
                 'latin-songs','dance-electronic-albums','hot-dance-airplay','dance-club-play-songs','dance-electronic-streaming-songs','dance-electronic-digital-song-sales',
                 'dance-electronic-songs','rhythmic-40','hot-adult-r-and-b-airplay','rap-albums','r-and-b-albums','r-b-hip-hop-albums','rap-streaming-songs','rap-song','r-and-b-streaming-songs',
                 'r-and-b-songs','r-and-b-hip-hop-streaming-songs','r-and-b-hip-hop-digital-song-sales','hot-r-and-b-hip-hop-airplay','r-b-hip-hop-songs',
                 'hard-rock-albums','hot-mainstream-rock-tracks','triple-a','alternative-albums','alternative-songs','rock-albums','rock-streaming-songs',
                 'rock-digital-song-sales','rock-airplay','rock-songs','americana-folk-albums','bluegrass-albums','country-albums','country-streaming-songs',
                 'country-digital-song-sales','country-airplay','country-songs','adult-pop-songs','adult-contemporary','pop-songs','heatseekers-albums',
                 'tastemaker-albums','catalog-albums','independent-albums','vinyl-albums','digital-albums','top-album-sales','on-demand-streaming-songs','twitter-emerging-artists',
                 'twitter-top-tracks','summer-songs','streaming-songs','digital-song-sales','radio-songs','billboard-200','hot-100']

for v in range(85,len(billboardname)):
    try:
        masterartists = []
        mastersongs = []
        masterytlinks = []
        masteryttitles = []
        lwsongs = []
        lwtitles = []
        lwartists = []
        lwlinks = []
        dates = []
        date = []
        def _helper(v):
            for w in range(0, 60):
                for z in range(20, 32):
                    page = requests.get(
                        "http://www.billboard.com/charts/" + billboardname[v] + "/" + year[w] + "-" + month[11] + "-" + day[
                            z] + "")
                    print(billboardname[v] + year[w] + "-" + month[11] + "-" + day[z])
                    print(str(page))
                    # print(str(page))
                    if str(page) == '<Response [200]>':
                        print(year[w])
                        global startyear
                        startyear = w - 1
                        print(startyear)
                        print(year[startyear])
                        return


        _helper(v)
        for x in range(startyear,60):
            for y in range(0,12):
                for z in range(1,32):
                    print(year[x] + '-' + month[y] + '-' + day[z])
                    artists = []
                    songs = []
                    ytlinks = []
                    yttitles = []
                    # print("http://www.billboard.com/charts/hot-100/" + year[x] + "-" + month[y] + "-" + day[z] + "")
                    page = requests.get("http://www.billboard.com/charts/" + billboardname[v] + "/" + year[x] + "-" + month[y] + "-" + day[z] + "")
                    # print(page)
                    print(str(page))
                    # print(str(page))
                    if str(page) == '<Response [404]>':
                        print('eli 404')
                        continue
                    if str(page) == '<Response [503]>':
                        print('eli 503')
                        continue

                    soup = BeautifulSoup(page.content, 'html.parser')

                    for link in soup.find_all("div", {"class":"chart-row__title"}):
                        print("Billboard scrape")
                        songstring = link.h2.text
                        songstring.strip()
                        songs.append(songstring)
                        if link.a is None:
                            artiststring = link.h3.text
                            artiststring = artiststring.strip()
                            artists.append(artiststring)
                        else:
                            artiststring = link.a.text
                            artiststring = artiststring.strip()
                            artists.append(artiststring)
                        youturl = "https://www.youtube.com/results?search_query=" + artiststring + " " + songstring + ""
                        try:
                            indx = lwsongs.index(songstring)
                            print('copy from last')
                            print(indx)
                            ytt = lwtitles[indx]
                            youtlink = lwlinks[indx]
                            yttitles.append(ytt)
                            ytlinks.append(youtlink)
                        except ValueError:
                            print("YTscrape")
                            page = requests.get(youturl)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            for link in soup.find("h3", {"class": "yt-lockup-title"}):
                                ytlink = link.get('href')
                                ytlink = str(ytlink)
                                youtlink = 'youtube.com' + ytlink
                                print(youtlink)
                                ytt = link.get('title')
                                ytt = str(ytt)
                                print(ytt)
                                yttitles.append(ytt)
                                ytlinks.append(youtlink)
                                break
                            continue

                    masterartists.append(artists)
                    mastersongs.append(songs)
                    masterytlinks.append(ytlinks)
                    masteryttitles.append(yttitles)
                    lwsongs = songs
                    lwartists = artists
                    lwlinks = ytlinks
                    lwtitles = yttitles
                    date = '' + year[x] + '-' + month[y] + '-' + day[z] + ''
                    date = [str(date),'']
                    print(date)
                    dates.append(date)

        print(masterartists)
        import csv

        with open('{0}-artists.csv'.format(billboardname[v]), 'w', encoding='utf8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(masterartists)
        with open('{0}-songs.csv'.format(billboardname[v]), 'w', encoding='utf8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(mastersongs)
        with open('{0}-yttitles.csv'.format(billboardname[v]), 'w', encoding='utf8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(masteryttitles)
        with open('{0}-ytlinks.csv'.format(billboardname[v]), 'w', encoding='utf8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(masterytlinks)
        with open('{0}-dates.csv'.format(billboardname[v]), 'w', encoding='utf8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(dates)
    except BaseException as e:
        print('Failed to do something: ' + str(e))
        continue