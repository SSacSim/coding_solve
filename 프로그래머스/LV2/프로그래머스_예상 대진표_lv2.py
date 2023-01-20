n = 8
a = 2
b = 3

A = a
B = b
if a > b :
  temp = a
  A = b
  B = temp

print(A,B)

# 이분탐색으로 search
start = 0
end = n
count = 0
i = 0
while True:

  mid = (start + end) // 2 # 중간

  if start >= end:
    break
  
  print("start,mid,end",start,mid,end)

  if (A <= mid) and (B > mid): # 서로 벌어져있을때
    print("실행")
    target = end - start
    find = 1
    print(target,find)
    while target >= find:
      find *=2
      count +=1
    break
    
  
  elif (A <= mid) and (B <=mid) : #둘다 mid보다 작을때
    end = mid
  elif (A >= mid) and (B >=mid):
    start = mid