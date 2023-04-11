class Tree:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Tree(100)
left = Tree(50)
right = Tree(150)
left2_left = Tree(25)
right2_left = Tree(75)
left2_right = Tree(125)
right2_right = Tree(175)

root.left = left
root.right = right
left.left = left2_left
left.right = right2_left
right.left = left2_right
right.right = right2_right

def bfs(root):
    current = root
    layer_lst = [current]
    c = 0
    while layer_lst:
        lst = []
        for x in layer_lst:

            if x.left:
                lst += [x.left]
            if x.right:
                lst += [x.right]
        layer_lst = lst
        c += 1
        print([x.val for x in layer_lst])
bfs(root)

def dfs(root):
    if root is None:
        return

    dfs(root.left)
    #print(root.val)
    dfs(root.right)

dfs(root)