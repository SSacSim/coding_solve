n = 4
left = 7
right = 14

start_row = left // n  # 1 
end_row = right // n  # 3


answer = []

start_count = start_row * n # 4 
for i in range(start_row, end_row + 1): # 1~ 3까지 row
    if start_count > (n**2):
        break
    for j in range(0,n): # columns
        if j <= i :
            now_num = i + 1
        else:
            now_num = j + 1
        print("now_num",now_num)
        
        if (start_count >= left) and (start_count <= right):
            answer.append(now_num)
        start_count +=1

print(answer)
    