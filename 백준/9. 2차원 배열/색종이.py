matrix = [[ 0 for _ in range(0,101)] for _ in range(0,101)]
time = int(input())
count = 0
for _ in range(time):
    x , y = map(int,input().split(" "))
    
    for i_x in range(0,10):
        for i_y in range(0,10): 
            temp = matrix[x + i_x][y + i_y] 
            if temp == 0:
                matrix[x + i_x][y + i_y] = 1
                count += 1
                
print(count)            


