import sys
from collections import Counter

input = sys.stdin.readline

_ = int(input())
input_list = list(map(int,input().strip().split(" ")))
my_counter = Counter(input_list)

_ = int(input())

result = []

num_list = list(map(int,input().strip().split(" ")))

for i in num_list:
    result.append(my_counter[i])
print(*result)
