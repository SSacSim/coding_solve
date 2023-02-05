n = 110011
k = 10

def chagne_number(n , k):
    number = n
    temp = []
    while True:
        if number == 0: 
            temp.reverse()
            return temp
        temp.append(number % k)
        number //= k
        
change_num = chagne_number(n, k)
change_num.append(0)

now_num = ""
count = 0
for i in change_num:
    if i == 0:
        # 소수인지 판별
        if now_num == "":
            continue
        int_now_num = int(now_num)
        print("int_now_num",int_now_num)
        flag = 0
        for j in range(2, int(int_now_num ** (1/2))+1 ):
            print("now_num,j",int_now_num,j)
            if int_now_num % j == 0:
                flag = 1
                break
        if flag != 1 and int_now_num != 1:
            count += 1
        now_num = ""
    else:
        now_num += str(i)
    print("======================")

print(count)
