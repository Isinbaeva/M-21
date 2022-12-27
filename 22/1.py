from pprint import pprint
import random
def make_bingo():
  vars = random.sample(range(1, 76), k=25)
  card = []
  for i in range(5):
    start = i * 5
    end = start + 5
    line = vars[start:end]
    if i == 2:
      line[2] = 0
    card.append(tuple(line))
  return tuple(card)


res = make_bingo
pprint(res)