
# December, 1st. Maximum depth of binary tree.
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_dec1(object):
    def recursiveDepth(self, current_node, count):
        """For the current node, if it is not None, updates de counter variable and calls itself for the left and right nodes"""
        if current_node is None:
            return count
        return max(self.recursiveDepth(current_node.left, count + 1), self.recursiveDepth(current_node.right, count + 1))
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursiveDepth(root, 0)

#--------------------------------------------------------

# December, 2nd. Definition for singly-linked list.
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution_2(object):

    def __init__(self, head):
        """
        Creates an instance of the class and counts the number of elements in the list.
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        current_node = head
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        self.counter = counter
        self.head = head

    def getRandom(self):
        """
        Takes a random number and returns the value in that element of the list
        Returns a random node's value.
        :rtype: int
        """
        random_index = random.randrange(self.counter)
        current_node = self.head
        for i in range(random_index):
            current_node = current_node.next
        return current_node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

#--------------------------------------------------------

# December, 3rd. Increasing order search tree.
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost
# node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def recursiveAdd(self, node_list, current_node, current_index):
        """Recursive function to traverse the tree (DFS). Adds each value of the node to a list on the left side of its
        parent if it is the first child and to the right if it is the second"""
        if current_node.left is not None:
            node_list.insert(current_index, current_node.left.val)
            node_list, current_index = self.recursiveAdd(node_list, current_node.left, current_index)
            current_index += 1
        if current_node.right is not None:
            node_list.insert(current_index+1, current_node.right.val)
            node_list, current_index = self.recursiveAdd(node_list, current_node.right, current_index+1)
        return node_list, current_index
    def increasingBST(self, root):
        """
        Gets a list with values of the nodes in the requested order and then creates a new tree
        using that order.
        :type root: TreeNode
        :rtype: TreeNode
        """
        node_list, index = self.recursiveAdd([root.val], root, 0)
        print(node_list)
        root_new = TreeNode(node_list[0])
        current = root_new
        for i in range(1,len(node_list)):
            current.right = TreeNode(node_list[i])
            current = current.right
        return root_new

test_root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
sol = Solution()
new_tree = sol.increasingBST(test_root)
current_new = new_tree
while current_new is not None:
    print(current_new.val)
    current_new = current_new.right

