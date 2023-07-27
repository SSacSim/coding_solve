# 메모리 초과 발생
# copy 때문인듯 
# copy말고 다른 방식으로 풀어야 할듯 
import sys
input = sys.stdin.readline 
N , M = map(int,input().strip().split(" "))
num_list = list(map(int,input().strip().split(" ")))
plus_list = list(map(int,input().strip().split(" ")))
matrix = {}
matrix[0] = 0

# 현재 보고 있는 index ( 메모리 값, 추가 비용)
for now_index in range(len(num_list)): 
    # 임시 matrix 생성 > 그때그때마다 바뀌면 안되기때문에 
    temp_matrix = matrix.copy()

    # temp_matrix에 들어있는 값들을 모두 볼것
    for matrix_key in matrix.keys():
        # 만약, (matrix_key + num_list[now_index) : Memory 값임  가 temp_matrix에 없으면 생성하여 넣어줌
        # 메모리값 not in matirx
        if matrix_key + num_list[now_index] > M:
            continue
        if (matrix_key + num_list[now_index]) not in temp_matrix:
            temp_matrix[matrix_key + num_list[now_index]] = (temp_matrix[matrix_key] + plus_list[now_index])
        # 메모리값이 존재함 = 추가비용이 이미 존재함
        else:
            if temp_matrix[matrix_key + num_list[now_index]] > (temp_matrix[matrix_key] + plus_list[now_index]):
                temp_matrix[matrix_key + num_list[now_index]] = (temp_matrix[matrix_key] + plus_list[now_index])
    matrix = temp_matrix.copy()

print(matrix[M])
