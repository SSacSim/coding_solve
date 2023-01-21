citations = [1,1,5,7,6]

citations.sort()
citations.reverse()

max_value = max(citations)
flag =  0
answer = 0
for i in range(max_value , -1, -1):
  print(i)
  count = 0
  for value in citations:
    if value >=i :
      count += 1
      
    if count >= i :
      answer = i
      flag =1
  
  if flag == 1:
    break
print(answer)