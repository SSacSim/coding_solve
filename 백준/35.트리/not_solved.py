class node_:
    def __init__(self , input_num = None):
        self.num = input_num
        self.left = None
        self.right = None

class my_tree:
    def __init__(self , node = None):
        self.root =None

    def insert(self , node):
        if self.root == None:
            self.root = node
        else:
            while True:
                if self.root.num > node.num:
                    
                break
            # left
              
            # right 
        pass
    def search(self):  
        pass

tree = my_tree(node_(30))
        


