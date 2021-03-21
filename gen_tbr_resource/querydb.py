from pymongo import MongoClient
from urllib.parse import quote_plus


class DB:
  
  def __init__(self, lang, config):
    user = config["user"]
    password = config["password"]
    host = config["host"]
    authdb = config["authdb"]
    uri = "mongodb://{}:{}@{}/{}".format(quote_plus(user), quote_plus(password), host, authdb)
    self.client = MongoClient(uri)
    self.prod_db = self.client["prod_"+lang+"2cn"]
    self.preprod_db = self.client[lang+"2cn"]

  def _search_base(self, vocabs):
    filtered = []
    for v in vocabs:
      dict_word = self.preprod_db.base.find_one({"word": v.lower()})
      if dict_word != None:
        del dict_word["_id"]
        filtered.append(dict_word)
    return filtered 

  def _search_extension(self, vocabs):
    collections = [cname for cname in self.preprod_db.collection_names() if cname not in ["base", "sentences", "vocabs"]]
    exts = {}
    for cname in collections:
      c = self.preprod_db[cname]
      exts[cname] = []
      for v in vocabs:
        dict_word = c.find_one({"word": v.lower()}) 
        if dict_word != None:
          del dict_word["_id"]
          exts[cname].append(dict_word)
    return exts

  def search(self, vocabs):
    vocabs_info = {}
    vocabs_info["base"] = self._search_base(vocabs)
    vocabs_info.update(self._search_extension(vocabs))
    return vocabs_info

  def exclude(self, vocabs):
    # TODO: return the vocabs which are not in base collection
    return vocabs

