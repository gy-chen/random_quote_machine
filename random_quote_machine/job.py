# coding: utf-8
from random_quote_machine.summary import summary
from random_quote_machine.video import extract_subtitles
from random_quote_machine.youtube import search_items_info, download
from random_quote_machine.model import Session, Video, Quote


def update_videos_from_youtube():
    """Update videos to database from Youtube search result

    :return:
    """
    # fetch the newest search result
    items = search_items_info()
    [_quote_and_save(item) for item in items if not _is_saved(item)]


def _is_saved(item):
    session = Session()
    saved_item = session.query(Video).filter(Video.title == item.title).one_or_none()
    return saved_item is not None


def _quote_and_save(item):
    downloaded_item = download(item.url)
    if downloaded_item.subtitle is not None:
        subtitles = extract_subtitles(downloaded_item.subtitle)
        quotes = summary(subtitles)
        # save to database
        video = Video(title=item.title, url=item.url)
        for quote in quotes:
            q = Quote(quote=quote, video=video)
            video.quotes.append(q)
        session = Session()
        session.add(video)
        session.commit()
    # TODO remove files

