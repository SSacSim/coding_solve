storey = 105

count = 0
while True:
    if storey == 0:
        break
    
    temp = storey % 10
    storey = storey //10
    
    print(temp)
    print(storey)
    if temp > 5 : # 5보다 크면 
        count += 10-temp
        storey += 1
    elif temp == 5:
        if storey % 10 >= 5:
            count += 10 - temp
            storey += 1
        elif storey % 10 < 5:
            count += temp
    else:
        count += temp    
    print("==============")

print(count)