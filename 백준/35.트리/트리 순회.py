import sys
input = sys.stdin.readline
N = int(input().strip())
matrix = {}

for _ in range(N):
    root , left, right = list(input().strip().split())

    matrix[root] = [left, right]
    
pre_order = []
mid_order = []
post_order = []

def circle_tree(node):
    if node == '.':
        return 
    pre_order.append(node)

    # left
    circle_tree(matrix[node][0])
    mid_order.append(node)
    # right
    circle_tree(matrix[node][1])
    post_order.append(node)
circle_tree("A")
print("".join(pre_order))
print("".join(mid_order))
print("".join(post_order))