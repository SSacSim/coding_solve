from collections import Counter

num = int(input())
num_list = list(map(int,input().split(" ")))
num_list.reverse()
list_count = Counter(num_list)
my_stack = [] # count , num 값 저장
answer= []
for i in num_list:
    
    while True:
        if len(my_stack) == 0:
            my_stack.append([list_count[i] , i ])
            answer.append(-1)
            break
            
        pop_numbers = my_stack.pop()
        if pop_numbers[0] > list_count[i]:
            answer.append(pop_numbers[1])
            my_stack.append(pop_numbers)
            my_stack.append([list_count[i], i])
            break
answer.reverse()
print(*answer)
        