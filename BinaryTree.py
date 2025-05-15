class Node:
    def __init__(self, value): # Contructor
        self.val = value
        self.left= None
        self.right = None

#In Binary Tree, each node has at most two children
#To create a node we need to create a class
#In this case, we are creating a class called Node


# Every Node in the tree should be reachable from the root node. if not its not a tree
# There shouldnt be any cycles in the tree
# The root node is the topmost node in the tree

#The Height of the tree is the height of the root node
#The depth of node is the number of edges from the root node to the node
#Height and depth goes inversely

#inorder traversal
#There are twio types of Traversals, DFS and BFS.

#DFS is depth first search and BFS is breadth first search

#In DFS , if there is children nodes to explore, Exploring them is priority.

#In BFS , Visiting node on the same level is priority before visisting Trail nodes.

#in DFS, 
#pre-oredr Traversal:
#1. Visit the root node
#2. Visit the left child until there are no more left children
#3. Visit the right child 
#inorder Traversal:
#1. Visit the left child
#2. Visit the root node
#3. Visit the right child
#post-order Traversal:
#1. Visit the left child
#2. Visit the right child
#3. Visit the root node


#Insert Node into Tree

#We will need to keep moving down the tree until we find a open spot.
# How long it takes to find a open sopt?
#It takes O(log n) time to find a open spot in a balanced tree which is height of tree
#A Binary tree holds pow(2,n) nodes at level n

#Binary Tree Practice

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.preorder_search(self.root, find_val):
            return True
        return False
       
        
    # def print_tree(self):
    #     """Print out all tree nodes
    #     as they are visited in
    #     a pre-order traversal."""
    #     return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        if start.value == find_val:
            return True
        
        else:
            if start.left:
                self.preorder_search(start.left, find_val)
            if start.right:
                self.preorder_search(start.right, find_val)
        
        return False
            

    # def preorder_print(self, start, traversal):
    #     """Helper method - use this to create a 
    #     recursive print solution."""
    #     return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
# print tree.print_tree()