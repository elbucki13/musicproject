import billboard_new
import csv
import json
import datetime
billboardname = ['youtube']
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
        while chart.previousDate:
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

        thefile = open('' + chartlist + ' json_commas.txt', 'w')
        for item in toCSV:
            thefile.write("%s,,," % item)
        # thefile.write("]")
        thefile.close()
        # Assuming res is a flat list
        with open('dates2.csv', "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in innerlist:
                writer.writerow(val)
        with open('dates22.csv', "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in outlist:
                writer.writerow(str(val))
        with open("output.csv", 'w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerow(outlist)
    except Exception as e:
        print('last')
        print(e)

