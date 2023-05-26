import sys
input =sys.stdin.readline
N, M = map(int,input().strip().split(" "))

matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().strip().split(" "))))
    
chick_location = []
house_location = []
for row in range(N):
    for column in range(N):
        if matrix[row][column] == 2:
            chick_location.append([row,column])
        if matrix[row][column] == 1:
            house_location.append([row,column])
            
from itertools import combinations

total_lenth = 9999999999
for combination_list in combinations(chick_location,M):
    house_location_memo = [ 9999999 for _ in range(len(house_location))]
    for in_location in combination_list:
        for index, i in enumerate(house_location):
            temp = abs(i[0] - in_location[0]) + abs(i[1] - in_location[1])
            if house_location_memo[index] > temp:
                house_location_memo[index] = temp
        if sum(house_location_memo) < total_lenth:
            total_lenth = sum(house_location_memo)        
print(total_lenth)
        
        