matrix = []
max_len = 0
for i in range(5)
    temp = list(input())
    matrix.append(temp)
    if max_len  len(temp)
        max_len = len(temp)
   
answer = []

for i in range(max_len) # colum
    for j in range(len(matrix))
        try
            answer.append(matrix[j][i])
        except
            continue
print(.join(answer))