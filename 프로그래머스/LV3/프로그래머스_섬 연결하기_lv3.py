n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
node_parent = [i for i in range(n)]
costs.sort(key = lambda x : x[2])

# kruskal 알고리즘 
def union(node1,node2,parent):
    node_parent[node1] = parent
    node_parent[node2] = parent
def find(node):
    if node_parent[node] == node :
        return node
    else:
        return_node = find(node_parent[node])
        return return_node
    
count = 0
answer = 0
for i in costs:
    # [0,1,1], [1,3,1]
    node1 = i[0]
    node2 = i[1]
    
    node1_p = find(node1)
    node2_p = find(node2)
    
    print("node1",node1)
    print("node2",node2)
    
    print("node1_p",node1_p)
    print("node2_p",node2_p)
    if node1_p != node2_p:
        print("유니온")
        union(node1_p,node2_p ,min(node1_p,node2_p))
        answer += i[2]
    
    if count == n-1:
        break
    
    print(" *************변경 후 ")
    print(node_parent)
    print("==================================")

print(answer)