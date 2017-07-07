import billboard_new
import csv
import json
chartlist = 'country-airplay'
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
outlist = []
toCSV = []
for b in range(0,len(billboardname)):
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
                chart = billboard_new.ChartData(chartlist, chart.previousDate)
                for a in range(0,len(chart.entries)):
                    eli = chart[a].to_JSON()
                    innerlist.append(eli)
                    del eli
                outlist.insert(0,innerlist)
                innerlist = []
                eli2 = chart.to_JSON()
                toCSV.insert(0, eli2)
                del eli2
                # print(chart.previousDate)
            except Exception as ex:
                print(ex)
                print('No more charts for '+billboardname[b])
                break


        print('writing files for ' + billboardname[b])
        with open("entries for " + chartlist + ".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(outlist)


        thefile = open('charts - ' + chartlist +'.txt', 'w')
        for item in toCSV:
            thefile.write("%s\n" % item)
    except Exception as e:
        print('last')
        print(e)