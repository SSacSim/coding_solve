from collections import Counter

weights = [100, 100, 100, 200, 200, 200]
weights_store = dict(Counter(weights))

ratio_store = ['23','24','32','34','42','43']

count = 0
for i in weights_store:
    print(i)
    for j in ratio_store:
        left = i * int(j[0])
        if left % int(j[1]) != 0:
            continue
        right = left //int(j[1])
        
        print("left,right",left,right)
        if right in weights_store:
            count += weights_store[i] * weights_store[right]
            print("추가된것 " , i , right)
    print("=================")

count = count // 2
for i in weights_store:
    count += int(weights_store[i] * (weights_store[i]-1) / 2 )

print(count)