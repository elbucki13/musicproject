import billboard_new
import csv
import json
import datetime
billboardname = ['hot-100']
outlist = []
trycount = 0
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
        while chart.previousDate != '2017-06-03':
            try:
                chart = billboard_new.ChartData(chartlist, chart.previousDate)
                eli2 = chart.to_JSON()
                toCSV.insert(0, eli2)
                del eli2
                print(chart.previousDate)
                innerlist.append(chart.previousDate)
                outlist.append(chart.date)
                # if chart.previousDate is None:
                #     print('None problem')
                #     if trycount < 1:
                #         year, month, day = map(int, chart.date.split('-'))
                #         passedDate = datetime.date(year, month, day)
                #         chart.previousDate = str(passedDate - datetime.timedelta(days=14))
                #         trycount = 1
                #     continue
            except Exception as ex:
                print(ex)
                print('No more charts for ' + billboardname[b])
                break


        print('writing files for ' + billboardname[b])


        thefile = open('' + chartlist + ' dates_new.csv', 'w')
        for item in outlist:
            thefile.write("%s\n" % item)
        # thefile.write("]")
        thefile.close()

    except Exception as e:
        print('last')
        print(e)

