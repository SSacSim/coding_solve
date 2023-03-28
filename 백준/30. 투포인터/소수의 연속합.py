target = int(input())
matrix = [0 for _ in range(target + 1)]
#소수 구하기
for i in range(2,target + 1):
    for j in range(2,target + 1):
        if i*j < len(matrix):
            if matrix[i * j] == 0:
                matrix [i * j] = 1
        else:
            break
sosu = []
for index, i in enumerate(matrix):
    if index > 1 and i == 0:
        sosu.append(index)
sosu = [0] + sosu
left_point = 1
right_point = 1

if target == 1:
    print(0)

else:
    total_sum = sosu[1]
    count = 0
    while True:
        if total_sum < target:
            right_point += 1
            if left_point >len(sosu) - 1  or right_point >len(sosu) - 1  : 
                break
            total_sum += sosu[right_point]
        elif total_sum > target:
            total_sum -= sosu[left_point]
            if left_point >len(sosu) - 1  or right_point >len(sosu) - 1  : 
                break
            left_point += 1
        else:
            count +=1
            right_point += 1
            if left_point >len(sosu) - 1  or right_point >len(sosu) - 1  : 
                break
            total_sum += sosu[right_point]
    print(count)  