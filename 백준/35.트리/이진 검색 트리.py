import sys      
sys.setrecursionlimit(30000)
input = sys.stdin.readline


class node_:
    def __init__(self , input_num = None):
        self.num = input_num
        self.left = None
        self.right = None

class my_tree:
    def __init__(self):
        self.root =None

    def insert(self , node):
        # root 가 None일때 
        node = node_(node)
        if self.root == None:
            self.root = node
        

        # root가 존재할때 
        else:
            # find을 진행하며 자식 노드가 없을경우 넣음.
            now_node = self.root
            while True: 
                if (now_node.num > node.num):  # 왼쪽에 넣음
                    if (now_node.left == None):
                        now_node.left = node
                        break
                    else:
                        now_node = now_node.left
                elif (now_node.num < node.num):  # 왼쪽에 넣음
                    if (now_node.right == None):
                        now_node.right = node
                        break
                    else:
                        now_node = now_node.right
    def post_search(self,root_node):
        if root_node == None:
            return 
        self.post_search(root_node.left)
        self.post_search(root_node.right)
        print(root_node.num)
tree = my_tree()
        
num_list =[]
while True:
    try:
        num_list.append(int(input()))
    except:
        break
for i in num_list:
    tree.insert(i)
tree.post_search(tree.root)
