number_list = []
total = 0
for i in range(5):
  temp = int(input())
  number_list.append(temp)
  total += temp
number_list.sort()
print(int(total /5) )
print(number_list[2])
