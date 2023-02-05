k = 1
d = 5

count = 0
d2 = d**2 
for i in range(0 , d+1):
    now_x = i * k
    
    if now_x > d:
        break
    print("now_x",now_x)
    temp = ((d2 - now_x ** 2) ** (1/2))// k
    print(int(temp))
    print("================")
    count += int(temp)+1    

print(count)
