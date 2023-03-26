import sys
input = sys.stdin.readline
N,C = map(int,input().split(" ")) # N : input 갯수 , M : 나누는 값
num_list = []
for _ in range(N):
  num_list.append(int(input()))
num_list.sort()
temp = num_list[0]
for i in range(len(num_list)):
  num_list[i] -= temp
diff_list =  [ num_list[x+1] - num_list[x] for x in range(len(num_list ) - 1)]
left = num_list[0]
right = num_list[-1]


max_answer = 0
while True:
  if left > right:
    break
  mid = (right + left) // 2

  # (C-1) * mid 가 전체 범위를 넘으면 다시 mid 조정
  if (C-1) * mid > num_list[-1] - num_list[0] :
    right = mid - 1
    
  # 이론상 mid * (C - 1)이 범위안에 C개 들어올 수 있는 경우
  else:
    count = 0
    nujeok = 0
    for x in diff_list:
      nujeok += x
      if nujeok >= mid:
        count += 1
        nujeok = 0
    if count >= C - 1:
      if max_answer < mid:
        max_answer = mid
      left = mid +1 
    else:
      right = mid -1

print(max_answer)
