import sys
input = sys.stdin.readline

K = int(input())
num_list = list(map(int,input().strip().split(" ")))
find = int(input())
find_list = list(map(int,input().strip().split(" ")))

max_sum = 40000

matrix = [False for _ in range(max_sum + 1 )]
matrix[0] = True

for pl_mi in num_list:
    temp = matrix.copy()
    for now_num in range(len(matrix)):
        if matrix[now_num] == False:
            continue
        else:
            if ((now_num + pl_mi) <= max_sum ):
                temp[now_num + pl_mi] = True
            if (abs(now_num - pl_mi) <= max_sum):
                temp[abs(now_num - pl_mi)] = True
    matrix = temp.copy()

answer = []
for i in find_list:
    if matrix[i]:
        answer.append("Y")
    else:
        answer.append("N")
print(*answer)
