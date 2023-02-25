n =3
matrix =[[ 0 for i in range(n)] for _ in range(n)]
matrix[0][0] = 1
now_num = 2 
now_x = 0
now_y = 0
flag_1 , flag_2, flag_3  = 0 ,0 , 0
while True:
    if flag_1 == flag_2 == flag_3 == 1 or n== 1:
        break
    
    # 세로
    for i in range(1,n):
        now_x += 1
        if now_x < n and now_y < n and matrix[now_x][now_y] == 0:
            print('dddd')
            matrix[now_x][now_y] = now_num
            now_num +=1
        else:
            if i== 1:
                print('dfgdfg')
                flag_1 = 1
            now_x -= 1 
            break
    if flag_1 == 1 :
        break
    print("세로",matrix)
    #가로
    for i in range(1,n):
        now_y += 1
        if now_x < n and now_y < n and matrix[now_x][now_y] == 0:
            matrix[now_x][now_y] = now_num
            now_num +=1
        else:
            if i== 1 :
                flag_2 = 1
            now_y -= 1
            break
    print("가로",matrix)
    if flag_2 == 1 :
        break
    #좌상 대각선
    for i in range(1,n):
        now_x -=1
        now_y -=1
        if now_x < n and now_y < n and matrix[now_x][now_y] == 0:
            matrix[now_x][now_y] = now_num
            now_num +=1
        else:
            if i== 1:
                flag_3 = 1
            now_x += 1
            now_y += 1
            break
    print("대각",matrix)
    if flag_3 == 1 :
        break
    print(flag_1, flag_2, flag_3)
answer =[]
for i in matrix:
    for j in i:
        if j != 0:
            answer.append(j)

print(answer)