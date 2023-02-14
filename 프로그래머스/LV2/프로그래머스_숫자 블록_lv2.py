begin = 1
end = 10

# 소수 판별
answer = []
for i in range(begin , end +1) : 
  print("i",i)
  max_temp = 0
  if i == 1:
    answer.append(0)
    continue
  for j in range(int(i ** (1/2)) , 0 , -1):
    if j > 10000000:
      continue
    if i % j == 0:
      if j == 1:
        if max_temp == 0:
          max_temp = 1
      else:
        temp1 = j
        temp2 = i // j
        
        if temp1 > 10000000:
          temp1 = 1
        if temp2 > 10000000:
          temp2 = 1
        print("dd", j , i // j )
        temp = max(j , i // j )
        if temp > max_temp:
          max_temp = temp
  answer.append(max_temp)
       
print(answer)     
