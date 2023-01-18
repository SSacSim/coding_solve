brown = 8
yellow = 1

total_num = brown + yellow
row = total_num // 3
columns = 3

answer = 0
for i in range(columns , row + 1):
    print(total_num)
    print(i)

    if total_num % i == 0:
        print("row",row)
        row = total_num // i
        print(row)
        print("=================")        
        temp = (row - 2) * (i -2) 
        if temp == yellow:
            answer = [row , i]
            break
print(answer)