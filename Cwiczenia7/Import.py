def read_file(filename) ->str:
  file = open(filename, encoding="utf8")
  content = file.read().splitlines()
  return content