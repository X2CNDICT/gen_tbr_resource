import spacy

class Parser:

  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  def __init__(self, lang):
    self.lang = lang
    self._nlp = spacy.load(self.__class__.pkgindices[lang], exclude=["parser", "ner", "lemmatizer", "textcat"])

  def vocabs(self, text):
    doc = self._nlp(text)
    excluded = ['SYM', 'X', 'NUM', 'PUNCT', 'SPACE']
    return list(set([e.text for e in doc if e.pos_ not in excluded]))

