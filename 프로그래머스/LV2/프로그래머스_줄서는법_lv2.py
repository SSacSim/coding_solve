n = 3
k = 5

total_number = 1
for i in range(n,1,-1):
    total_number *= i

use_list = [1 for i in range(n + 1)]
use_list[0] = 0    
total_number


answer = []
def line_find(leave_num , temp):
    print("============================")
    calcum = temp
    leave_user = sum(use_list)
    
    print("leave_num", leave_num)
    print("누적",calcum)
    print("use_list",use_list)
    if leave_user == 1 : # 마지막 하나를 제외한 모든 것을 사용했을때
        return 
    
    print("남은 사람",leave_user)
    
    one_ = leave_num // leave_user  # one_ 하나당 나올 수 있는 가지수
    print("한사람당 가지수",one_)
    for i in range(1, n + 1):
        if use_list[i] == 1:
            calcum += one_
            
            print("임시 calcum",calcum)
            if calcum >= k:
                global answer
                answer.append(i)
                use_list[i] = 0
                print("들어가는 temp",calcum - one_)
                line_find(one_ , calcum - one_)
                break
            
    return 0
    
line_find(total_number,0)


for index, i in enumerate(use_list):
    if i == 1:
        answer.append(index)

print(list(map(int,answer)))

