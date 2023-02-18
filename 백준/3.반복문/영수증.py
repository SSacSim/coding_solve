target = int(input())
buy_number = int(input())

for i in range(buy_number):
  temp = list(map(int,input().split(" ")))
  target -= (temp[0] * temp[1])

answer = "Yes" if target ==0 else "No"
print(answer)

