from youtubesearchpython import VideosSearch as vs
from bs4 import BeautifulSoup as bs
from pytube import Playlist as pl
import os
import requests as r
import re
import json

def search(title:str, num:int=None, idsOnly=False, titleOnly=False, playlist=False, *args, **kwargs):

    if not playlist:

        if not num:
            num = 5

        if "youtube.com" in title or "youtu.be" in title:
            num = 1

        # initialize lists (yes it hurts to look at, i know)
        thumbs, cthumbs, durs, views, channels, titles, fulltitles, ids = [], [], [], [], [], [], [], []

        # search for video and add data to lists
        for video in vs(title, limit=int(num)).result()['result']:

            thumbs.append(video['thumbnails'][0]['url'])
            cthumbs.append(video['channel']['thumbnails'][0]['url'])
            durs.append(video['duration'])
            views.append(video['viewCount']['short'])

            # cut off channel/title if too long
            if len(video['channel']['name']) > 25:
                channels.append(video['channel']['name'][:22] + "...")
            else:
                channels.append(video['channel']['name'])
            
            fulltitles.append(video['title'])

            if len(video['title']) > 40:
                titles.append(video['title'][:37] + '...')
            else:
                titles.append(video['title'])
            
            ids.append(video['id'])
        
        if idsOnly:
            return ids
        elif titleOnly:
            return titles
        else:
            return thumbs, cthumbs, durs, views, channels, titles, fulltitles, ids
    
    else:

        if "spotify.com" in title:

            return "spotify"
            # spotify downloading is managed with spdl
        
        elif "youtube.com" in title or "youtu.be" in title:

            idList = []
            
            for url in pl(title):
                idList.append(url.split("=")[1])
            
            return idList
        
        else:

            return ("error", "playlist")




# YVS VIDEO RESULT FORMAT

{
    'type': 'video',
    'id': '2ZIpFytCSVc',
    'title': 'Bruh Sound Effect #2',
    'publishedTime': '6 years ago',
    'duration': '0:02',
    'viewCount':
    {
        'text': '27,914,126 views', 'short': '27M views'
    },
    'thumbnails':
    [
        {
            'url': 'https://i.ytimg.com/vi/2ZIpFytCSVc/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAYHTc2j9kqEi8idTXfcITHk2Xb9g',
            'width': 360,
            'height': 202
        },
        {
            'url': 'https://i.ytimg.com/vi/2ZIpFytCSVc/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCOMBKHf7tZoVJ4bIizNlJDvE1_SA',
            'width': 720,
            'height': 404
        }
    ],
    'richThumbnail': None,
    'descriptionSnippet':
    [
        {
            'text': 'Leave A Like And Subscribe To Keep Up On The Latest New Free Sound Effects.'
        }
    ],
    'channel':
    {
        'name': 'Jame Benedict',
        'id': 'UCU8N6si9tf2OBSonH_B9Hxg',
        'thumbnails':
        [
            {
                'url': 'https://yt3.ggpht.com/ytc/AMLnZu8RG1lBREM_wDw0lXC7hQpJF_p0dZ2dlBqBsACw=s68-c-k-c0x00ffffff-no-rj',
                'width': 68,
                'height': 68
            }
        ],
        'link': 'https://www.youtube.com/channel/UCU8N6si9tf2OBSonH_B9Hxg'
    },
    'accessibility':
    {
        'title': 'Bruh Sound Effect #2 by Jame Benedict 6 years ago 2 seconds 27,914,126 views',
        'duration': '2 seconds'
    },
    'link': 'https://www.youtube.com/watch?v=2ZIpFytCSVc',
    'shelfTitle': None
}