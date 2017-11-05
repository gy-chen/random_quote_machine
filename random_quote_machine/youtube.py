# coding: utf-8
"""
Youtube

  - Search youtube for speech videos.

  - Download youtube videos and subtitles
"""
import os
import youtube_dl
import youtube_dl.utils
from collections import namedtuple, ChainMap
from googleapiclient.discovery import build
from random_quote_machine import setting

YoutubeDownloadResult = namedtuple('YoutubeDownloadResult', ['filename', 'subtitle'])
YoutubeSearchItemInfo = namedtuple('YoutubeSearchItemInfo', ['url', 'title'])

API_KEY = setting.YOUTUBE_API_KEY
YOUTUBE_BASE_URL = 'https://www.youtube.com/watch?v='


def search(**kargs):
    """Search Youtube videos

    by default this method search Religion related videos. The behavior of this method can be overwrited by keyword
    arguments using keywords that specific in Youtube list API document.

    :param kargs:
    :return:
    """
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    return youtube.search().list(
        part='snippet',
        order='relevance',
        topicId='/m/06bvp',
        type='video',
        relevanceLanguage='en',
        **kargs
    ).execute()


def search_items_info(**kargs):
    """Search and extract items info

    :param kargs: See search
    :return: list of YoutubeItemInfo nametuple
    """
    search_result = search(**kargs)
    items = extract_youtube_items(search_result)
    return extract_youtube_items_info(items)


def extract_youtube_items(search_result):
    """Extract youtube search result's items

    :param search_result:
    :return: list of search result item
    """
    return search_result['items']


def extract_youtube_items_info(items):
    """Extract youtube item info from search result items

    :param items:
    :return: list of YoutubeSearchItemInfo nametuple
    """
    result = [YoutubeSearchItemInfo(extract_youtube_url(item), extract_youtube_title(item)) for item in items]
    return result


def extract_youtube_url(item):
    """Extract youtube url from item of search result

    :param item:
    :return:
    """
    return YOUTUBE_BASE_URL + item['id']['videoId']


def extract_youtube_title(item):
    """Extract youtube video's tite from item of search result

    :param item:
    :return: title of the Youtube video item
    """
    return item['snippet']['title']


def download(youtube_url, **options):
    """Download the specific youtube video and subtitle

    :param youtube_url:
    :param options: same usage as argument in search function. See search
    :return: (filename, subtitle) filenames of downloaded videos and subtitles
    """
    ydl_options = {
        'writesubtitles': True,
        'format': 'worstvideo'
    }
    ydl_options = ChainMap(options, ydl_options)
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(youtube_url)
        filename = ydl.prepare_filename(info)
        subtitle = youtube_dl.utils.subtitles_filename(filename, 'en', 'vtt')
        subtitle = subtitle if os.path.exists(subtitle) else None
        return YoutubeDownloadResult(filename, subtitle)


def download_search(**kargs):
    """Search and download search result's videos and subtitles

    :param kargs: keyword arguments to overwrite search parameters
    :return: [(filename, subtitle),... ]
    """
    search_result = search(**kargs)
    result = [download(extract_youtube_url(item)) for item in extract_youtube_items(search_result)]
    return result
