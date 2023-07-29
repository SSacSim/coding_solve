from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().strip().split(" ")))
M = int(input())
M_list = list(map(int,input().strip().split(" ")))

my_dic = defaultdict(int)
for i in N_list:
  my_dic[i] = 1
answer = []
for i in M_list:
  if my_dic[i] == 0:
    answer.append(0)
  else:
    answer.append(1)
print(*answer)
