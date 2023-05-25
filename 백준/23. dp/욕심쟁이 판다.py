import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())

    # num_list = [[3,2],[1,4],[4,1],[2,3],[5,5]]
    num_list = []

    for _ in range(N):
        num_list.append(list(map(int,input().strip().split(" "))))

    num_list.sort()
    count = 1
    target = num_list[0][1]
    for i in range(1,N):
        if target > num_list[i][1]:
            count += 1
            target = num_list[i][1]
            
    print(count)