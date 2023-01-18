from collections import deque
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 4

start = 1
end = max(stones)
answer = 0
max_count = 0

while True:
  count = 0
  print(start,end)

  if start > end:
    break
  now_count = 0

  mid = (start + end) // 2
  print("mid",mid)
  
  # mid는 명수
  # 즉 mid수 만큼 사람이 지나갈때 이 배열은 지날갈 수 있는 배열인가?를 체크
  for i in stones:
    if mid > i:
      count += 1
    else:
      count = 0

    if now_count < count : # now_count는 못가는 돌 갯수
      now_count = count
  
  print("now_count",now_count)
  

  if now_count >= k: # 갈수 없는 인원수 
    end = mid -1

  else:
    print("now_count",now_count)
    print(answer)
    if mid >= answer:
      answer = mid
    start = mid +1
  
  print("max_count",max_count)
  print("=======================")

print(answer)