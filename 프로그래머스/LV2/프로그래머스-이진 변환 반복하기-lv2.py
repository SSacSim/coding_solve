s = "110010101001"
answer = 0
total_zero = 0
while True:
  zero_count = 0
  for i in s:
    if i == "0":
      zero_count += 1
  
  if s == "1":
    break
  s = bin(len(s) - zero_count)[2:]
  answer += 1
  total_zero += zero_count

answer = [answer,total_zero]
answer