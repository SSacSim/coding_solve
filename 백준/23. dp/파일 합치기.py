import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())

    num_list = list(map(int,input().strip().split(" "))) 
    # 파일 합치기
    # dp.. memozation 접근이 잘못됨. 

    # matirx : [ 단순합,  누적합]
    matrix = [[ [ num_list[row] , num_list[row] ]  if row == column else [999999999 , 999999999] for column in range(K)] for row in range(K)]
    for plus in range(K):
        for row in range(K - plus):
            column = row + plus
            for i in range(row ,column):
                value = 0
                temp = 0
                # 1개/1개일때 단순 더하기 
                if (row == i) & (column == (i+1)):
                    temp = matrix[row][i][0] + matrix[i+1][column][0] 
                else:
                    
                    if row == i:
                        temp += matrix[row][i][0] # 왼쪽 하나일때 
                        temp += matrix[i+1][column][0] # 오른쪽 다수일때 단순 합
                        ## 여기까지 하면, 최종 값이 나옴
                        # 그럼 오른쪽 다수의 누적합을 더해야함
                        temp += matrix[i+1][column][1] # 누적합을 더해줌
                    elif column == (i+1):
                        temp += matrix[row][i][0] # 왼쪽 다수일때 단순합
                        temp += matrix[i+1][column][0] # 오른쪽 다수일때 단순 합
                        ## 여기까지 하면, 최종 값이 나옴
                        # 왼쪽 다수의 누적합을 더해야함
                        temp += matrix[row][i][1] # 누적합을 더해줌
                    else:
                        # 왼쪽, 오른쪽이 단 하나의 원소만 가지지 않을 경우
                        # 왼쪽 단순합
                        temp += matrix[row][i][1]
                        # 오른쪽 단순합
                        temp += matrix[i+1][column][1]

                        # 왼/오 단순합을 더함 
                        temp += (matrix[row][i][0] + matrix[i+1][column][0])

                if matrix[row][column][1] >= temp :
                    matrix[row][column] = [ matrix[row][i][0] + matrix[i+1][column][0], temp]
    print(matrix[0][K-1][1])
