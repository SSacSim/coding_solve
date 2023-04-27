import sys
input = sys.stdin.readline
N, M = map(int,input().strip().split(" "))
word_dict = dict()
for _ in range(N):
  word_ = input().strip()
  if len(word_) >= M:
    if word_ not in word_dict:
      word_dict[word_] = 1
    else:
      word_dict[word_] += 1
temp = sorted(word_dict.items() , key = lambda item: (-item[1], -len(item[0]) , item[0]))
for i in temp:
  print(i[0])