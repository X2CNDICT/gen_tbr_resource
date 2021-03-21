import csv
import json

def write_to_csv(fields, content, csvfile="output.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)


class CSVWriter:
  def __init__(self, name):
    self.dstfile = name + '.csv'

  def encode(self, content):
    new_content = []
    for e in content:
      new_e = {}
      for k,v in e.items():
        new_e[k] = json.dumps(v) if not isinstance(v, str) and not isinstance(v, int) and v != None else v
      new_content.append(new_e)
    return new_content

  def write(self, content, options={}):
    _content = self.encode(content)
    keys = _content[0].keys() if len(_content) > 0 else []
    write_to_csv(keys, _content, self.dstfile)

