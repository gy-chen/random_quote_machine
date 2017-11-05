# coding: utf-8
"""Provides video related functions

- extract subtitles from subtitle file.

"""
import io
import pysrt


def extract_subtitles(filename, text_only=True):
    subtitles = pysrt.open(filename)
    if text_only:
        return [subtitle.text for subtitle in subtitles]
    return subtitles


def subtitles_to_text(subtitles):
    result = io.StringIO()
    for subtitle in subtitles:
        result.write(subtitle)
        result.write('\n')
    return result.getvalue()
