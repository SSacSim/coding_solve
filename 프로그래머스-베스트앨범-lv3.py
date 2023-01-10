genres =  ["classic", "pop", "classic", "classic", "classic"]
plays = [500, 1000, 400, 300, 200, 100]


record_map = dict()
count_map = dict()

for index, (i , j) in enumerate(zip(genres, plays)):
    # i = 장르 ,  j > 횟수,  index > genres안 index번호
    if i not in record_map: # 장르가 map에 없을시
        record_map[i] = [[j,index]]
        count_map[i] = j
    else:
        record_map[i].append([j,index])
        count_map[i] += j
print("===================")
print(record_map)
print(count_map)
print("===================")

dic_list = [] # 최대 재생수 정렬
for key, value in count_map.items():
    temp = [key,value]
    dic_list.append(temp)

dic_list.sort(key = lambda x : -x[1])
print(dic_list)

answer = []
for data in dic_list:
    genre = data[0]

    temp = record_map[genre]
    print(f"{genre} sort전 :", temp)
    temp.sort(key = lambda x : (-x[0], x[1]))
    print(f"{genre} sort후 :", temp)
    
    for i_index, i in enumerate(temp):
        if i_index >=2 :
            break
        answer.append(i[1])

print(answer)