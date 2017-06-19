import billboard_new
import csv
import json
import datetime
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


i = 0
toCSV = []
quant = False

for b in range(77,len(billboardname)):
    try:
        print('Running ' + billboardname[b] + ' charts')
        chartlist = billboardname[b]
        chart = billboard_new.ChartData(chartlist)
        print(chart)
        toCSV = []
        innerlist = []
        outlist = []
        chart.previousDate = chart.date
        while chart.previousDate:
            try:
                #print('trying ' + str(chart.previousDate))
                chart = billboard_new.ChartData(chartlist, chart.previousDate,quantize=True)
                print(chart)
                eli2 = chart.to_JSON()
                toCSV.insert(0, eli2)
                del eli2
                #print(chart.previousDate + 'is previous date')
            except AttributeError as Aex:
                if chart.previousDate is not None:
                    print(chart.previousDate)
                    year, month, day = map(int, chart.date.split('-'))
                    passedDate = datetime.date(year, month, day)

                    chart.previousDate = str(passedDate - datetime.timedelta(days=7))
                    continue
                print('att error')
                print(str(chart.previousDate))
                break
            except Exception as ex:
                print(ex)
                print('No more charts for '+billboardname[b] + str(chart.previousDate))
                # i = i + 1
                # quant=False
                # year, month, day = map(int, chart.date.split('-'))
                # passedDate = datetime.date(year, month, day)
                # if i < 100:
                #         chart.previousDate = str(passedDate - datetime.timedelta(days=i))
                #         print('new PD')
                #         print(' this is helper ' + str(chart.previousDate))
                #         print(chart.previousDate)
                #         continue
                # break


        print('writing files for ' + billboardname[b])

        thefile = open('' + chartlist + ' json_commas.txt', 'w')
        for item in toCSV:
            thefile.write("%s,,," % item)
        # thefile.write("]")
        thefile.close()
        quant = False

    except Exception as e:
        print('last')
        print(e)

