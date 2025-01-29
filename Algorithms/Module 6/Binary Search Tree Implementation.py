# Binary Search Tree

class Node:
    def __init__(self, data, left=None, right=None):
        #Create Node with data and children
        self.data = data
        self.left = left
        self.right = right

    def compare(self, other_node):
        if self.data > other_node.data:
            return 2
        elif self.data < other_node.data:
            return 0
        elif self.data == other_node.data:
            return 1
        else:
            return -1

class Tree:
    def insertNode(self, root, newValue):
        if root == None:
            return Node(newValue)
        else:
            if root.data == newValue:
                return root
            if root.data < newValue:
                root.right = self.insertNode(root.right, newValue)
            else:
                root.left = self.insertNode(root.left, newValue)
            return root
            


    def deleteNode(self, root,  nodeValue):
        if root == None:
            return root
    
        if root.data > nodeValue:
            root.left = self.deleteNode(root.left, nodeValue)
            return root
        elif root.data < nodeValue:
            root.right = self.deleteNode(root.right, nodeValue)
            return root
    
        if root.left == None:
            temp= root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp
        
        else:
            replacementParent = root
            replacement = root.right
            while replacement.left != None:
                replacementParent= replacement
                replacement = replacement.left
            if replacementParent!= root:
                replacementParent.left = replacement.right
            else:
                replacementParent.right = replacement.right
            root.data = replacement.data
    
            return root
        
    

    def build_tree(self, array):
        sorted_array = sorted(list(set(array)))
        return self.build_tree_recursive(sorted_array)

    def build_tree_recursive(self, array):
        if not array:
            return None

        middle_index = len(array) // 2
        root = Node(array[middle_index])
        root.left = self.build_tree_recursive(array[:middle_index])
        root.right = self.build_tree_recursive(array[middle_index + 1:])
        return root
    
    def printTree(self, root):
        if root == None:
            return
        self.printTree(root.left)
        print(root.data)
        self.printTree(root.right)

    def __init__(self, number_array):
        self.root = self.build_tree(number_array)


new_tree = Tree([1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324])
new_tree.printTree(new_tree.root)
new_tree.deleteNode(new_tree.root, 7)
new_tree.insertNode(new_tree.root, 10)
print("\nNew Tree after removing 7 and adding 10")
new_tree.printTree(new_tree.root)