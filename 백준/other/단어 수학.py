import sys
input = sys.stdin.readline
n = int(input())
input_str_list = []
my_dict = {}
for _ in range(n):
    # input_str
    input_str = input().strip()
    input_str_list.append(input_str)
    len_input_str = len(input_str)
    for i in range( 0 , len_input_str):
        if input_str[i] not in my_dict :
            my_dict[input_str[i]] = 10 ** (len_input_str - i - 1 )
        else:
            my_dict[input_str[i]] += 10 ** (len_input_str - i - 1 )
            
list_dict = list(my_dict.items())
list_dict.sort(key = lambda x : x[1] , reverse = True)

new_dict = {}
number = 9
for i in list_dict:
   new_dict[i[0]] = number
   number -= 1
answer = 0
for i in input_str_list:
    temp = ""
    for j in i:
        temp += str(new_dict[j])
        
    answer += int(temp)
print(answer)