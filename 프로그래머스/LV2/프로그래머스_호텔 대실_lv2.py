book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]

time_to_number = []

for i in book_time:
    start_time = i[0].split(":")
    end_teim = i[1].split(":")
    
    time_to_number.append([int(start_time[0]) * 60 + int(start_time[1]) , int(end_teim[0]) * 60 + int(end_teim[1]) + 10])

time_to_number.sort()

room = []
for i in time_to_number: # 예약손님
    print("i",i)
    flag = 0
    for j_index, j in enumerate(room): # 이미 사용하고있는손님
        print("j_index, j",j_index,j)
        if j[1] <= i[0]:
            room[j_index] = i
            flag = 1
            break
    if flag == 0:
        room.append(i)
    print("room",room)
    print("==================")

print(len(room))