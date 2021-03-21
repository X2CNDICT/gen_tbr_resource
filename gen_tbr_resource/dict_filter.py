from gen_tbr_resource import DB

class DictFilter:

  def __init__(self, lang, config):
    self.lang = lang
    self.db = DB(lang, config)

  def query(self, vocabs):
    filtered = self.db.exclude(vocabs)
    result = self.db.search(filtered)
    return result
