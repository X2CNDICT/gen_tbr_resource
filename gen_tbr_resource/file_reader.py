import webvtt
import re

def filter_typos(sentence):
  filtered = sentence.replace("♪","").replace("\n", " ").replace("-", "").replace("\t", " ")
  filtered = re.sub(r'[\[\{].*[\}\]]:?', "", filtered).replace("  ", " ")
  return filtered.strip()


class FileReader:

  def __init__(self, filename, filetype):
    self.filename = filename
    self.filetype = filetype
    self._get_text = {
      "srt": self.srt_text,
      "plain": self.plain_text
    }

  def text(self):
    return self._get_text[self.filetype]()

  def srt_text(self):
    obj = webvtt.from_srt(self.filename)
    content = " ".join([filter_typos(caption.text) for caption in obj.captions])
    return content 

  def plain_text(self):
    content = ""
    with open(self.filename, "r") as handler:
      content = handler.read()
    return content 
