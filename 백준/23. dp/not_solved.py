# 메모리, 시간 초과
# DP를 사용해서 메모리, 시간 초과를 해결해야함.
# 어떤 방식으로 메모를 할 것인가 고민

import sys
input = sys.stdin.readline
K = int(input())
num_list = list(map(int,input().strip().split(" ")))
find = int(input())
find_list = list(map(int,input().strip().split(" ")))

# 양팔저울

result = set()
def dp(left, right ,number_index ):
    if right > left :
        result.add(right - left)
    if number_index >= len(num_list):
        return
    # 추가 없는쪽(오른쪽)에 놓았을때
    dp(left, right + num_list[number_index] , number_index + 1)
    # 추가 있는쪽에 놓았을때
    dp(left + num_list[number_index] , right , number_index + 1)
    # 아무것도 안할때
    dp(left,right , number_index + 1)
    
dp(0,0,0)

answer = []
for i in find_list:
    if i in result:
        answer.append("Y")
    else:
        answer.append("N")
print(*answer)
