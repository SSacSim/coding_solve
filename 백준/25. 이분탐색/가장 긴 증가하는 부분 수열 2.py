n = int(input())
num_list = list(map(int,input().split(" ")))
def look_index(store, i):
    left = 0
    right = len(store) - 1
    temp = 0
    while True:
        if left > right:
            return temp
        mid = (right + left) // 2 # index를 나타냄
        
        if store[mid] > i:
            temp = mid
            right = mid -1 
        elif store[mid] == i:
            return mid
        else:
            left = mid +1

store = []
for i in num_list:
    if len(store) == 0: # 맨 처음 비어있을 경우 
        store.append(i)
        continue
    
    if i > store[-1]:
        store.append(i)
    elif i < store[-1]:
        find_index = look_index(store, i)
        store[find_index] = i
    
print(len(store))    
