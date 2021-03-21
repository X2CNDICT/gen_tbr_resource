from gen_tbr_resource import FileReader, Parser, DictFilter, CSVWriter
import click
import json
import os

@click.command()
@click.option("--filename", help="Specify the input file", prompt="filename")
@click.option("--filetype", help="Specify the file is srt or plain", prompt="filetype", default="plain")
@click.option("--lang", help="Specify the language", default="en", prompt="language")
@click.option("--dstname", help="Specify the output folder name", prompt="dstname")
def file2vocabs(filename, filetype, lang, dstname):
  
  reader = FileReader(filename, filetype)
  text = reader.text()

  phase = {"step": 1, "msg": "Finish Reading file"}
  print(json.dumps(phase), flush=True)

  
  parser = Parser(lang)
  vocabs = parser.vocabs(text)

  phase = {"step": 2, "msg": "Finish vocabs parsering"}
  print(json.dumps(phase), flush=True)

  dbconfig =  {
    "user": "dict",
    "password": "turingmachine",
    "host": "127.0.0.1",
    "authdb": "admin"
  }

  dict_filter = DictFilter(lang, dbconfig)
  vocabs_info = dict_filter.query(vocabs)

  phase = {"step": 3, "msg": "Finish vocabs dictionary lookup"}
  print(json.dumps(phase), flush=True)

  for category, v in vocabs_info.items():
    if not os.path.exists(dstname):
      os.makedirs(dstname)
    csv_writer = CSVWriter(dstname+"/"+category)
    csv_writer.write(v)

  phase = {"step": 4, "msg": "Finish csv saving"} 
  print(json.dumps(phase), flush=True)

