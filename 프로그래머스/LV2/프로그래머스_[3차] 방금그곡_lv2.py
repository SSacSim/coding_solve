m = "ABC"
musicinfos =["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def exchange_shap(akbo):
  temp = []
  for index, n in enumerate(akbo):
      if n == "#":
        temp[len(temp) - 1] += "#"
        continue
      temp.append(n)
  return temp

m = exchange_shap(m)
answer = "(None)"
print(m)
max_len = 0
for i in musicinfos:
  print("max_len",max_len)
  i = i.split(",")
  temp = i[0].split(":")
  temp1 = int(temp[0]) * 60 + int(temp[1])
  temp = i[1].split(":")
  temp2 = int(temp[0]) * 60 + int(temp[1])

  time = temp2 - temp1
  print("time",time)

  akbo = exchange_shap(i[3])
  print("exchage akbo",akbo)
  akbo *= (time // len(akbo)) + 1
  akbo = akbo[:time]
  print("increase akbo",akbo)
  
  #check 음표
  for k in range(len(akbo) - len(m) + 1):
    flag = 0 # 일치하면 0 / 일치하지 않으면 1
    for k2 in range(len(m)):
      print(akbo[k + k2] , m[k2])
      if akbo[k + k2] != m[k2] :
        flag = 1
        break
    print("flag",flag)
    if flag == 0:
      print("==============================")
      if max_len < time:
        answer = i[2]
        max_len = time
      break

print(answer)