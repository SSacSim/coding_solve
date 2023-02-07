n = 5
money = [1,2,5]

answer_list = [0 for _ in range(n + 1)]
answer_list[0] = 1

for i in money:
    for j in range(1,len(answer_list)):
        if j < i :
            continue
        
        answer_list[j] += answer_list[j - i]

print(answer_list[n])