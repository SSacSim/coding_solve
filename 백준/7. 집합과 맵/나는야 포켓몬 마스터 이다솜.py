import sys
input = sys.stdin.readline
my_dict_str= dict()
my_dict_int= dict()

Q , A = map(int, input().split(" "))

for i in range(Q):
    input_str = input().strip()
    my_dict_str[input_str] = i+1
    my_dict_int[i+1] = input_str

answer = []
for i in range(A):
    input_Q = input().strip()
 
    if (input_Q[0] >= "0") and (input_Q[0] <= "9") : # 숫자일경우
        answer.append(my_dict_int[int(input_Q)])
    else:
        answer.append(my_dict_str[input_Q])

for i in answer:
   print(i)