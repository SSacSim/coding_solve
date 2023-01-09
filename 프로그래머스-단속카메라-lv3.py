routes = [[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]
# 가장 범위가 넓은 것 정렬
routes.sort(key=lambda x : x[1])
print("정렬 후:", routes)

visit = []

for i in routes:
    print("i",i)
    print("visit",visit)
    temp = []
    flag = 0
    
    if len(visit) == 0:
        visit.append(i) # 아직 어느것도 만나지 않았을때
        continue
    for j in visit: 
        if ( i[0] <= j[0] ) and (i[1] >= j[1]):
            flag= 1
            continue
        elif (i[0] <= j[0]) and (i[1] >= j[0] ): # j0 가 i0 ~ i1 사이에 있을때
            flag= 1
            continue
        elif (i[0] <= j[1]) and (i[1] >= j[1] ): # j1 가 i0 ~ i1 사이에 있을때
            flag= 1
            continue

    if flag == 0:
        visit.append(i)
        
print("종료",visit)
print(len(visit))
