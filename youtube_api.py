#!/usr/bin/python


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyC4Bv926rlGgzcJPah5CgRglxNofFCosoU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search_api(artist,title):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_string = string_search = artist.replace("&", "") + " " + title
    search_response = youtube.search().list(
        q=string_search,
        part="id,snippet",
        maxResults=3
        ).execute()

    video_title = []
    video_id = []
    print(string_search)

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_title.append(search_result["snippet"]["title"])
            video_id.append(search_result["id"]["videoId"])

    if len(video_id) >= 1:
        return {'returned_link': video_id[0], 'returned_ytt': video_title[0]}
    else:
        return {'returned_link': '', 'returned_ytt': ''}



# if __name__ == "__main__":
#   # default="Google"
#
#
#   # string_search = "Justin Bieber"
#   # argparser.add_argument("--q", help="Search term", default=string_search)
#   # argparser.add_argument("--max-results", help="Max results", default=1)
#   # args = argparser.parse_args()
#   # print(args)
#
#   try:
#     eb = youtube_search_api(get_args("Justin Bieber","Despacito"))
#     print('debug')
#     print(eb)
#     print(eb['returned_link'] + " " + eb['returned_ytt'])
#   except HttpError:
#     print("An HTTP error occurred:\n%s" )

