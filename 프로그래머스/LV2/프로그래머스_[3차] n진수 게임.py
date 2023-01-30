n = 16 # 진수
t = 16 # 말해야되는 갯수
m = 2 # 사람 수
p = 2 # 시작순서 

def jinbub(number,n):
  temp = number
  result = ""

  while True:
    if temp%n >=10:
      result += chr(55 + temp%n)
    else:
      result += str(temp % n)
    temp = temp //n 

    if temp == 0:
      break
  return "".join(reversed(result))

now_num = 0
answer = ""
while True:
  if (len(answer)//(m)) >= t:
    break

  answer += jinbub(now_num,n)
  now_num += 1

result = ""
for i in range(-1+p, len(answer) , m):
  print(i)
  if len(result) == t:
    break
  result +=answer[i]

print(result)