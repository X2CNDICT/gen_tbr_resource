from gen_tbr_resource import DictFilter


def test_dict_filter():
  vocabs = ['Giants', 'of', 'the', 'deep', 'hear', 'me', 'I', 'thought', 'you', "'d", 'see', 'it', 'my', 'way', 'Help', 'me', 'kill', 'Zeus', 'and', 'I', "'ll", 'make', 'the', 'sea', 'yours', 'again', 'No', 'Let', 'me', 'pass', 'Would', 'you', 'have', 'preferred', 'I', 'left', 'him', 'there', 'Why', 'are', 'you', 'here', 'Hera', "'s", 'gone', 'too', 'far', 'I', "'m", 'here', 'to', 'join', 'you', 'if', 'you', "'ll", 'have', 'me', 'She', 'offered', 'them', 'your', 'need', 'you', 'to', 'do', 'thing', 'for', 'me', 'Kneel'] 

  dbconfig =  {
    "user": "dict",
    "password": "turingmachine",
    "host": "127.0.0.1",
    "authdb": "admin"
  }
  dict_filter = DictFilter("en", dbconfig)
  vocabs_info = dict_filter.query(vocabs)
  print(vocabs_info)
  assert "base" in vocabs_info
