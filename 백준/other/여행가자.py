import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input()) # 도시 수
M = int(input())

city_list = [i for i in range(N + 1 )]
def find(k):
    if k != city_list[k]:
        k = find(city_list[k])
    return k 

def union(a,b): # a 가 root 가 될 것 
    pa = find(city_list[a])
    pb = find(city_list[b])
    
    city_list[pb] = pa

for k in range(1, N + 1 ) :
    p = list(map(int, input().split(" ")))
    
    for enum , i in enumerate(p):    
        if i == 1 :
            union(k,enum +1 )
    
p1 = list(map(int, input().split(" ")))


answer = None
answer2 = "YES"
for i in p1:
    if answer is None:
        answer = find(i)
    elif answer != find(i):
        answer2 = "NO"
        break
print(answer2)
