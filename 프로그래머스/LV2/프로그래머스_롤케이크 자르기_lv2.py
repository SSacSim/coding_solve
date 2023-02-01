topping = [1, 2, 3, 1, 4]

from collections import deque
from collections import Counter

left_q = deque([])
right_q = deque(topping)

set_left = dict(Counter())
set_right = dict(Counter(topping))

left_count = 0
right_count = len(set(right_q))

count = 0
while True:
    print("left",set_left)
    print("right",set_right)
    print("right",right_q)
    
    print(left_count)
    print(right_count)
    if len(right_q) == 0:
        break
    
    pop_number = right_q.popleft() # 하나 뻄
    
    if pop_number not in set_left:
        set_left[pop_number] = 1
        left_count +=1
        
    set_right[pop_number] -= 1
    
    if set_right[pop_number] == 0:
        right_count -= 1
        
    if right_count == left_count:
        count +=1
    
    print("===================")

print(count)