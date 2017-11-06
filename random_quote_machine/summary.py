# coding: utf-8

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from random_quote_machine.video import subtitles_to_text

nltk.download('punkt')

LANGUAGE = "english"
SENTENCES_COUNT = 3


def summary(subtitles, sentences_count=SENTENCES_COUNT):
    """Summary the subtitles

    :param subtitles: list of subtitle in string type.
    :param sentences_count: count the return sentences
    :return:
    """
    summarizer = Summarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = get_stop_words(LANGUAGE)

    subtitles_text = subtitles_to_text(subtitles)

    parser = PlaintextParser.from_string(subtitles_text, Tokenizer(LANGUAGE))

    return [str(sentence) for sentence in summarizer(parser.document, sentences_count)]
