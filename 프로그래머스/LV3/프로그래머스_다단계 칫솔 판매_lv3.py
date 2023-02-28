enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

my_d = dict()
pay_d = dict()
# dictionary을 이용하여 tree형태 구성 자식 : 부모 형태
for i,j in zip(enroll , referral):
  # i : 자식 / j : 부모
  my_d[i] = j
  pay_d[i] = 0 

my_d['-'] = []

for i,j in zip(seller , amount):
  value = j * 100
  now_name = i
  now_parent = my_d[i] 
  print("========================")
  print("시작점 name",now_name)
  print("시작점 parent",now_parent)  
  print("시작점 value",value)  
  while True:
    if now_name == '-':
      break
    if value < 1:
      break
   
    pay_d[now_name] += value - int(value * 0.1)
    value = int(value * 0.1)
    now_name = now_parent
    now_parent = my_d[now_name]

    print("name",now_name)
    print("parent",now_parent)  
    print("value",value)  
    print("******************")

print(list(pay_d.values()))
