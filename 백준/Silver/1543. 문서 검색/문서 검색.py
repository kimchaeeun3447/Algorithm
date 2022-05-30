document = input()
word = input()
idx = 0

def count(index):
  global idx
  if document.find(word, index) == -1:
    return 0
  else:
    idx = document.find(word, index) + len(word)
    if idx > len(document) - 1:
      return 1
    else:
      return 1 + count(idx)

print(count(idx))