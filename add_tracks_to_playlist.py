
import pprint
import sys

import spotipy
import spotipy.util as util
from find_entries import get_Spot_ids_JSON

# username = '12142287499'
username = 'Eli Brantingham'

import os
from json.decoder import JSONDecodeError

scope = 'playlist-modify-public'
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)



# token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    userinfo = sp.current_user()
    print(userinfo)
    username = userinfo['id']
    charttype = 'country-songs'
    top_rank = 1
    bottom_rank = 5
    playlist_name = '{} peakin at {} to {}'.format(charttype,top_rank,bottom_rank)
    results = sp.user_playlist_create(username, playlist_name, public=True)
    # results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
    print(results['id'])
    playlist_id = results['id']
    track_ids_master = get_Spot_ids_JSON(charttype,top_rank,bottom_rank,start_date='2000-01-01',end_date = 1)
    for x in range(len(track_ids_master)):
        track_ids = track_ids_master[x]
        results2 = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
else:
    print("Can't get token for", username)