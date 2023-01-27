scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
wan = scores[0]
scores.sort(key=lambda s: (-s[0], s[1])) # (가장큰 수 ,가장 작은 수)
count = 1
for i in scores:
  if wan[0] < i[0] and wan[1] < i[1]:
    answer = -1
    break
  
  max_value = 0
  if max_value <= i[1]:
    if(wan[0] + wan[1]) < (i[0] + i[1]):
      count +=1
    max_value = i[1]
print(count)
  