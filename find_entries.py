import json

# get artists from old json
# chartlist = 'country-streaming-songs'
# text_file = open('' + chartlist + ' with YT and Spotifyb Links.txt', "r")
#
# lines = text_file.read()
# eb = json.loads(lines)
# print(eb)
#
# eb1 = eb["country_strem"][2]
# print(len(eb["country_strem"]))
# spo_list = []
# entry_list = []
# artist_list = []
# title_list = []
# spo_list_repeat = []
# entry_list_repeat = []
# artist_list_repeat = []
# title_list_repeat = []
# repeat = 0
# keyval = 0
# print(eb1)
# for key, value in eb1.items():
#     print(key, value)
# for x in range(len(eb["country_strem"])):
#     helper = eb["country_strem"][x]["date"]
#     print(eb["country_strem"][x]["date"])
#     if helper == '2017-04-29':
#         print(x)
#         print(' is the year')
# print(eb["country_strem"][15]['entries'][13])
# for x in range(len(eb["country_strem"])):
#     for y in range(len(eb["country_strem"][x]['entries'])):
#         eb["country_strem"][x]['entries'][y]['numberoftime'] = 1
#         if eb["country_strem"][x]['entries'][y]['artist'] in artist_list and eb["country_strem"][x]['entries'][y]['title'] in title_list and eb["country_strem"][x]['entries'][y]['spotifyID'] in spo_list:
#             repeat = repeat + 1
#             eb["country_strem"][x]['entries'][y]['numberoftime'] = eb["country_strem"][x]['entries'][y]['numberoftime'] + 1
#             artist_list_repeat.append(eb["country_strem"][x]['entries'][y]['artist'])
#             title_list_repeat.append(eb["country_strem"][x]['entries'][y]['title'])
#             spo_list_repeat.append(eb["country_strem"][x]['entries'][y]['spotifyID'])
#             entry_list_repeat.append(eb["country_strem"][x]['entries'][y])
#             continue
#         artist_list.append(eb["country_strem"][x]['entries'][y]['artist'])
#         title_list.append(eb["country_strem"][x]['entries'][y]['title'])
#         spo_list.append(eb["country_strem"][x]['entries'][y]['spotifyID'])
#         entry_list.append(eb["country_strem"][x]['entries'][y])
#     helper = eb["country_strem"][x]["date"]
#     print(eb["country_strem"][x]["date"])
#     if helper == '2017-04-29':
#         print(x)
#         print(' is the year')
# print(entry_list)
# print(repeat)
# print(len(entry_list))
# print(title_list_repeat)
# print(eb)
# eb = json.dumps(eb)
# thefile2 = open('' + chartlist + ' debug.txt', 'w')
# thefile2.write(eb)
# text_file.close()
# get Spotify ids from top x  songs from y to z dates
def get_Spot_ids_JSON(chartname,top,end,start_date=1,end_date=1):
    spotID_list = []
    master_spotID_list = []
    text_file = open('' + chartname + ' with YT Links.txt', "r")
    lines = text_file.read()
    eb = json.loads(lines)
    print(eb[chartname][0])
    ebb = json.loads(eb[chartname][0])
    print(ebb)
    for y in range(0,len(eb[chartname])):
        ebb = json.loads(eb[chartname][y])
        print(ebb["date"])
        print(start_date)
        if ebb['date'] != start_date and start_date != 1:
            continue
        print(ebb['date'])
        start_date = 1
        for x in range(top-1,end):
            SPID = ebb['entries'][x]['spotifyID']
            if len(SPID) != 22:
                continue
            if SPID in spotID_list:
                continue
            spotID_list.append(ebb['entries'][x]['spotifyID'])
            if len(spotID_list) == 100:
                master_spotID_list.append(spotID_list)
                spotID_list = []
        if ebb['date'] != end_date and end_date != 1:
            break
    master_spotID_list.append(spotID_list)
    print(master_spotID_list)
    return master_spotID_list
if __name__ == "__main__":
    lister = get_Spot_ids_JSON('rock-songs',1,10)
    print(lister)
    print(len(lister))


