import billboard_new
import csv
import json
import datetime
from pathlib import Path
chartlist = 'country-airplay'
# #billboardname = ['next-big-sound-25','lyricfind-us','lyricfind-global','youtube','spotify-rewind','spotify-velocity','spotify-viral-50','france-songs',
#                  'german-albums','germany-songs','canadian-albums','hot-canada-digital-song-sales','canadian-hot-100','united-kingdom-albums','united-kingdom-songs',
#                  'china-v-chart','japan-hot-100','world-albums','soundtracks','reggae-albums','new-age-albums','jazz-songs','jazz-albums',
#                  'kids-albums','comedy-albums','classical-albums','blues-albums','holiday-songs','holiday-streaming-songs','holiday-albums','holiday-season-digital-song-sales',
#                  'hot-holiday-songs','gospel-albums','gospel-streaming-songs','gospel-digital-song-sales','gospel-airplay','gospel-songs','christian-albums',
#                  'christian-streaming-songs','christian-digital-song-sales','christian-airplay','christian-songs','tropical-albums','latin-pop-albums','regional-mexican-albums',
#                  'latin-albums','tropical-songs','latin-pop-songs','regional-mexican-songs','latin-streaming-songs','latin-digital-song-sales','latin-airplay',
#                  'latin-songs','dance-electronic-albums','hot-dance-airplay','dance-club-play-songs','dance-electronic-streaming-songs','dance-electronic-digital-song-sales',
#                  'dance-electronic-songs','rhythmic-40','hot-adult-r-and-b-airplay','rap-albums','r-and-b-albums','r-b-hip-hop-albums','rap-streaming-songs','rap-song','r-and-b-streaming-songs',
#                  'r-and-b-songs','r-and-b-hip-hop-streaming-songs','r-and-b-hip-hop-digital-song-sales','hot-r-and-b-hip-hop-airplay','r-b-hip-hop-songs',
#                  'hard-rock-albums','hot-mainstream-rock-tracks','triple-a','alternative-albums','alternative-songs','rock-albums','rock-streaming-songs',
#                  'rock-digital-song-sales','rock-airplay','rock-songs','americana-folk-albums','bluegrass-albums','country-albums','country-streaming-songs',
#                  'country-digital-song-sales','country-airplay','country-songs','adult-pop-songs','adult-contemporary','pop-songs','heatseekers-albums',
#                  'tastemaker-albums','catalog-albums','independent-albums','vinyl-albums','digital-albums','top-album-sales','on-demand-streaming-songs','twitter-emerging-artists',
#                  'twitter-top-tracks','summer-songs','streaming-songs','digital-song-sales','radio-songs','billboard-200','hot-100']
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

outlist = []
miss_count = 0
toCSV = []
for b in range(20,len(billboardname)):

    chartlist = billboardname[b]
    my_file = Path('' + chartlist + ' with dates.txt')
    if my_file.is_file():
        print('' + chartlist + ' with dates.txt exists')
        continue
    try:
        print('Running ' + billboardname[b] + ' charts')
        chart = billboard_new.ChartData(chartlist)
        print(chart)
        toCSV = []
        innerlist = []
        outlist = []
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
                    print('Charts cant load ' + billboardname[b] + str(dates[i]))
                    continue
                else:
                    break
            if len(chart.entries) > 5:
                eli2 = chart.to_JSON()
                toCSV.insert(0, eli2)
                del eli2
                miss_count = 0
            else:
                miss_count = miss_count + 1
                if miss_count > 100:
                    break
                print('no entires')
        miss_count = 0




        print('writing files for ' + billboardname[b])

        thefile = open('' + chartlist + ' with dates.txt', 'w')
        for item in toCSV:
            thefile.write("%s,,," % item)
        # thefile.write("]")
        thefile.close()
    except Exception as e:
        print('last')
        print(e)

