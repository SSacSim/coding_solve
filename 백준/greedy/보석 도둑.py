# heapq를 사용하여 보석의 수를 줄이는게 가장 큰 핵심 
# 현재 bag에 들어갈 수 있는 가장 가치가 큰 보석을 찾으면,
# 찾은 곳까지의 보석은 볼 필요가 없기때문에 N번 반복하여 보석을 찾을 수 있음.
import heapq
import sys
input = sys.stdin.readline
N, K = map(int,input().strip().split(" "))

boseok = []
for _ in range(N):
    heapq.heappush(boseok, list(map(int,input().strip().split(" "))))
bag = []
for _ in range(K):
    bag.append(int(input().strip() )) # 가방 사용무게 , 사용여부 ( 1 : 사용가능 / 0 : 사용불가능)

bag.sort()
stack_value = []
total_sum = 0
for now_bag in bag:
    while boseok :
        if now_bag >= boseok[0][0]:
            heapq.heappush(stack_value, -boseok[0][1])
            heapq.heappop(boseok)
        else:
            break
    if stack_value:
        total_sum -= heapq.heappop(stack_value)    
print(total_sum)