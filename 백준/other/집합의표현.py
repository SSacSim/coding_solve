import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# 유니온 define
n,m = map(int,input().split(" "))

index_list = [ i for i in range(n +1 )]
def find(number):
    if number == index_list[number]:
        return number
    index_list[number] = find(index_list[number])
    return index_list[number]
    
    
def union(a , b ):
    root_a = find(a)
    root_b = find(b)
    index_list[root_a] = root_b
    
    
for _ in range(m):
    q , a , b = map(int, input().split(" "))
    
    if q == 0:
        union(a,b)
    else: 
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
