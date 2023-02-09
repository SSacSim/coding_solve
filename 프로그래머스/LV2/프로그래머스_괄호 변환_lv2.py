p = "()))((()"

def change_(w):
  print("===============================in recursive ")

  if w == "":
    print("반환")
    temp = ""
    return temp
  temp_stack = []

  # u , v 나누 
  check_bal = 0
  for index , i in enumerate(w): # 
    if i == "(":
      check_bal += 1
    else:
      check_bal -= 1
    
    if check_bal == 0 or index == (len(p) -1): 
      u = w[:index+1]
      v = w[index+1:]
      break
  print("w" , w)
  print("u",u)
  print("v",v)

  # u의 올바른 괄호 문자열 판단
  temp_u = []
  flag = 0 # 0 > 올바른 문자열 / 1 > 올바르지 않은 문자열
  for i in u:
    if i == "(":
      temp_u.append("(")
    else :
      if len(temp_u) == 0:
        flag =1
        break
      
      pop_str = temp_u.pop()
      if pop_str ==")":
        flag = 1
        break
    print("temp_u",temp_u)
  if len(temp_u) != 0:
    flag = 1
  
  print("flag",flag)

  if flag == 0: # 올바른 문자열일 경우 
    print("올바른 문자열 ")
    return_str = change_(v)
    print("반환된 올바른 문자열" , return_str)
    return u + return_str
  else: # 올바른 문자열이 아닌경우 
    print("올바르지 않은  문자열 ")
    change_str = "("
    return_str = change_(v)
    print("return_str_올바르지 않음",return_str)
    change_str += (return_str + ")")
    
    temp_u = ""
    for j in u[1:-1]:
      if j == "(":
        temp_u += ")"
      else:
        temp_u += "("
    change_str += temp_u
    print("최종 return" , change_str)
    return change_str
    
return_p = change_(p)
print(return_p)
