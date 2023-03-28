_, _ = map(int,input().split(" "))

A = set(list(map(int,input().split(" "))))
B = set(list(map(int,input().split(" "))))

tempA = A.difference(B)
tempB = B.difference(A)

print(len(tempA) + len(tempB))
