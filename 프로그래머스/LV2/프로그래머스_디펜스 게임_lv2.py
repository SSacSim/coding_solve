n = 7
k = 3
enemy =[4, 2, 4, 5, 3, 3, 1]

enemy = [ -i for i in enemy]

import heapq
accum_num = 0
accum_list = []
answer = -1
heapq.heapify(accum_list)
for index, i in enumerate(enemy) :
    print("i" , i )
    accum_num -= i
    heapq.heappush(accum_list,i)
    
    
    if accum_num > n:
        if k != 0:
            pop_number = heapq.heappop(accum_list)
            accum_num += pop_number
            k -= 1
    
    print(accum_num)
    print(accum_list)
    print("k", k)
    if k == 0 and accum_num > n:
        print("break!!!!")
        answer = index
        print(index)
        break
    print("=====================")

if answer == -1:
        answer = len(enemy)
print(answer)