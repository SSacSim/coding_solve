record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

id_dict = dict()

for i in record:
  print(i.split( ))
  temp = i.split()
  if temp[0] == "Enter":
    id_dict[temp[1]] = temp[2]
  elif temp[0] == "Change":
    id_dict[temp[1]] = temp[2]  

answer = []
for i in record:
  temp = i.split()
  if temp[0] == "Enter":
    answer.append(f"{id_dict[temp[1]]}님이 들어왔습니다.")
  elif temp[0] == "Leave":
    answer.append(f"{id_dict[temp[1]]}님이 나갔습니다.")

print(answer)