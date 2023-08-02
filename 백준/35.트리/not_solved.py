
task = 0
task = 0
while True:
    task += 1
    n , m = map(int,input().strip().split(" "))
    if (n == 0) and (m == 0):
        break
    inf = 0
    matrix = [ [] for _ in range(n + 1)]
    flag = [ 0 for _ in range(n + 1)]

    notree_flag = 0
    for i in range(m):
        start , end = map(int,input().strip().split(" "))
        if i == 0:
            matrix[start].append(end)
        else:
            matrix[start].append(end)
    flag = [ 0 for _ in range(n + 1)]
    count = 0

    for i in range(1,n+1):
        start = i
        if flag[start] == 1:
            continue
        if (len(matrix[start]) == 0) and flag[start] == 0:
            flag[start] = 1
            count +=1
        if len(matrix[start])>=2:
            flag[start] = 1
            for j in matrix[start]:
                flag[j] = 1
            continue
        elif len(matrix[start]) == 1 :
            while True:
                flag[start] = 1
                if len(matrix[start]) == 0:
                    count += 1
                    break
                if len(matrix[start]) == 1:           
                    start = matrix[start][0]
                else:
                    break
                if flag[start] == 1:
                    break
    if count == 0:
        print(f"Case {task}: No trees.")
    elif count == 1 :
        print(f"Case {task}: There is one tree.")
    else:
        print(f"Case {task}: A forest of {count} trees.")
