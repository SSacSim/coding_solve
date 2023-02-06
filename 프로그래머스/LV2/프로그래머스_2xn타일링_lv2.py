n = 4
cal_list = []
for index , i in enumerate(range(1,n+1)):
  if i == 1 or i ==2 :
    cal_list.append(i)
    continue

  cal_list.append(cal_list[index-2] + cal_list[index-1])
print(cal_list[-1])