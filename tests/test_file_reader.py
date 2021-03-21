from gen_tbr_resource import FileReader


def test_read_srt_file():
  srt_file_reader = FileReader("tests/subtitle.srt", "srt")
  content = srt_file_reader.text()
  print(content) # pytest -rP
  assert  len(content) > 0

def test_read_plain_file():
  plain_file_reader = FileReader("tests/plain.txt", "plain")
  content = plain_file_reader.text()
  print(content) # pytest -rP
  assert len(content) > 0 

