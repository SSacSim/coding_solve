import sys
input = sys.stdin.readline

from collections import deque
play_count = int(input())
stack_list = deque([])

for _ in range(play_count):
    # print("==============================")
    
    play_list = list(input().split())
    
    
    
    if play_list[0] == "push":
        stack_list.append(play_list[1])
        
    elif play_list[0] == "front":
        if len(stack_list) == 0:
            print("-1")
        else:
            print(stack_list[0])
    elif play_list[0] == "back":
        if len(stack_list) == 0:
            print("-1")
        else:
            print(stack_list[-1])
            
    elif play_list[0] == "size":
        print(len(stack_list))

    elif play_list[0] == "empty":
        if len(stack_list) == 0:
            print("1")
        else:
            print("0")

    elif play_list[0] == "pop":
        if len(stack_list) == 0:
            print("-1")
        else:    
            print(stack_list.popleft())
    
    # print(stack_list)
        
