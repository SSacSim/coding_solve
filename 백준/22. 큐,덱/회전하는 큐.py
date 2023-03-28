n, m = list(map(int, input().split()))
choice = list(map(int, input().split()))
idx = list(range(1, n+1))
count = 0

while True:
    if not choice:
        print(count)
        break
    if idx.index(choice[0]) == 0:
        idx.pop(0)
        choice.pop(0)
    else:
        if idx.index(choice[0]) > len(idx)/2:
            idx.insert(0, idx[-1])
            idx.pop(-1)
            count += 1
        else:
            idx.append(idx[0])
            idx.pop(0)
            count += 1
