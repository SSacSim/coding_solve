import heapq
import sys
input =sys.stdin.readline
    
TC = int(input().strip())
for _ in range(TC):
    N, M, W  = map(int,input().strip().split(" "))
    matrix = []

    for _ in range( M):
        input_temp = list(map(int,input().strip().split(" ")))
        
        matrix.append([ input_temp[0] , input_temp[1] ,input_temp[2]])
        matrix.append([ input_temp[1] , input_temp[0] ,input_temp[2]])

    for _ in range( W):
        input_temp = list(map(int,input().strip().split(" ")))
        
        matrix.append([ input_temp[0] , input_temp[1] , -input_temp[2]])
    
    inf = 9999999999
    memo = [ inf for _ in range(N + 1)] #1base
    s = matrix[0][0]
    memo[s] = 0
    flag = 0 
    for i in range(1, N + 1):
        updata_flag = 0
        
        for next_ in matrix:
            start_node = next_[0]
            end_node = next_[1]
            length = next_[2]

            if memo[end_node] > memo[start_node] + length:
                updata_flag = 1
                memo[end_node] = memo[start_node] + length
        
        if i == N :
            if updata_flag == 1 : # update가 없으면... 
                flag = 1
            break

    if flag == 1:
        print("YES")
    else:
        print("NO")