numbers = [2,7]

answer = []
for number in numbers :
    row_num_list = list(bin(number)[:1:-1]) + ['0']
    num_list = list(bin(number)[:1:-1]) + ['0']
    # 바뀐 수 만들기
    for index , i in enumerate(num_list[:-1]):
        if i == '0':
            num_list[index] = '1'
            break
        else:
            num_list[index] = '0'
            num_list[index + 1] = str(int(num_list[index +1]) + 1)
        print("===================")
        
    
    count = 0
    for i , j in zip(num_list, row_num_list):
        if i != j :
            count += 1

    print("count",count)
            
    if count <=2 :
        answer.append(int("".join(num_list[::-1]),2))

    else:
        for index , (i , j) in enumerate(zip(num_list, row_num_list)):
            print(index , i , j)
            if count <=2 :
                print("num_list",num_list[::-1])
                answer.append(int("".join(num_list[::-1]),2))
                break
            if i != j :
                print('바꾸기 전 ', num_list)
                num_list[index] = j
                count -= 1
                print('바꾼 후 ',num_list)
            print("====================")
        
print(answer)
                
            