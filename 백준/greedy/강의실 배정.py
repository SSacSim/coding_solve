import heapq
import sys
input = sys.stdin.readline
N = int(input().strip())

left_q = []
right_q = []
for _ in range(N):
    start , end = map(int,input().strip().split(" "))
    heapq.heappush(right_q, [start , end])
    
memo = []
for _ in range(len(right_q)):

    now_start , now_end = heapq.heappop(right_q)
    if len(memo) == 0:
        heapq.heappush(memo,now_end)
        continue
    
    else:
        pop_number = heapq.heappop(memo)
        
        if (pop_number <= now_end) and (now_start >= pop_number):
            heapq.heappush(memo, now_end)
        else:
            heapq.heappush(memo,pop_number)
            heapq.heappush(memo,now_end)
print(len(memo))
    