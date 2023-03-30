N , C = map(int,input().split(" "))
num_list = list(map(int,input().split(" ")))

# left / right 쪼갬
if N % 2 != 0:
  mid = int(N // 2 + 1)
else:
  mid = int(N//2)

left_num_list = num_list[:mid]
right_num_list = num_list[mid:] 


from itertools import combinations

left_sum_dict = [0]
right_sum_dict = [0]

for i in range(mid):
  for j in combinations(left_num_list, i + 1):
    temp_sum = sum(j)
    left_sum_dict.append(temp_sum)
for i in range(N-mid):
  for j in combinations(right_num_list, i + 1):
    temp_sum = sum(j)
    right_sum_dict.append(temp_sum)

right_sum_dict.sort()
answer = 0

for i in left_sum_dict:
  # right_sum은 이분 탐색 수행
  target = C - i
  start = 0
  end = len(right_sum_dict) -1
  last = 0
  k = 0

  while True:
    k += 1
    mid = (end + start) // 2

    if start > end:
      answer += mid +1
      break
    if right_sum_dict[mid] > target:

      end = mid - 1
    elif right_sum_dict[mid] <= target:

      start = mid + 1
      last = mid
print(answer)


