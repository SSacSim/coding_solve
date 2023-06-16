# 3 1 0 -3 -2 
import heapq

N = int(input().strip())

plus_list = []
zero_list = []
minus_list = []

for _ in range(N):
    temp_input = int(input().strip())
    if temp_input > 0 :
        heapq.heappush(plus_list , -temp_input)
    elif temp_input == 0:
        heapq.heappush(zero_list , temp_input)
    else:
        heapq.heappush(minus_list , temp_input)

plus_c = plus_list.copy()
zero_c = zero_list.copy()
minus_c = minus_list.copy()

# plus 
total = 0
while len(plus_c) >=2:
    left = -heapq.heappop(plus_c)
    right = -heapq.heappop(plus_c)
    
    # 둘중 하나라도 1인경우 그냥 더하기
    if left == 1 or right == 1:
        total += left + right
        continue
    else:
        total += (left * right)
        continue
if len(plus_c) >= 1 :
    total -= plus_c[0]

# minus 
while len(minus_c) >=2:
    left = heapq.heappop(minus_c)
    right = heapq.heappop(minus_c)
    
    # 모두 음수기때문에 곱하는게 가장 best
    total += (left * right)
    
if len(zero_c) == 0 and len(minus_c) >= 1:
    total += minus_c[0]
print(total)
