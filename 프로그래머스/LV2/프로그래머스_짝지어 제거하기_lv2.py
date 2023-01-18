
s = 'cca'
 
str_list = list(s)

answer = []
before_str = 0

for x in str_list:
    print("x",x)
    print(before_str)
    if before_str == 0: 
        before_str = x
        continue
    
    if before_str == x :
        if len(answer) == 0:
            before_str = 0
        else:
            before_str = answer.pop()
    else:
        answer.append(before_str)
        before_str = x 
    print(answer)
    print("==============")        

if before_str != 0:
    answer.append(before_str)
print(answer)
if len(answer) == 0:
    temp = 1
else:
    temp = 0