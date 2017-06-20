import json
chartlist = 'country-streaming-songs'
text_file = open('' + chartlist + ' with YT and Spotify Links.txt', "r")

lines = text_file.read().split(',,,')
text_file.close()
# lines = text_file.readlines()
print(lines)
print(len(lines))
jsonlist = []
for x in range(len(lines)-1):
    eb = json.loads(lines[x])
    jsonlist.append(eb)
    print(eb)
print(jsonlist)
# thefile = open('' + chartlist + ' with YT and Spotifya Links.txt', 'w')
# thefile.write(jsonlist)
# text_file.close()


new_dict = dict()
new_dict['country_strem'] = jsonlist
ebb = json.dumps(new_dict)
print(ebb)
thefile2 = open('' + chartlist + ' with YT and Spotifyb Links.txt', 'w')
thefile2.write(ebb)
text_file.close()