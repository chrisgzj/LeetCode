
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
class Solution_3(object):
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

# test_root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
# sol = Solution()
# new_tree = sol.increasingBST(test_root)
# current_new = new_tree
# while current_new is not None:
#     print(current_new.val)
#     current_new = current_new.right

#--------------------------------------------------------

# December, 4th. The kth Factor of n
# Given two positive integers n and k.
#
# A factor of an integer n is defined as an integer i where n % i == 0.
#
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or
# return -1 if n has less than k factors.


class Solution_4(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        list_of_factors = []
        for i in range(1,n+1):
            if n % i == 0:
                list_of_factors.append(i)
        if len(list_of_factors) < k:
            return -1
        return list_of_factors[k-1]

#--------------------------------------------------------

# December, 5th. Can place flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot
# be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an
# integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
# rule.

class Solution_5(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        Traverses the list once and checks, for each place, if a plant can be located there.
        Separate if clauses for first and last position of the flowerbed, as well as edge cases.
        Edge cases: flowerbed empty or with only one plot.
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if flowerbed == []:
            return False
        if flowerbed == [0]:
            if n > 1:
                return False
            return True
        if flowerbed == [1]:
            if n == 0:
                return True
            return False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        for plot in range(1, len(flowerbed)-2):
            if flowerbed[plot] == 0 and flowerbed[plot - 1] == 0 and flowerbed[plot + 1] == 0:
                flowerbed[plot] = 1
                n -= 1
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[0] = 1
            n -= 1
        if n <= 0:
            return True
        return False

sol = Solution_5()
print(sol.canPlaceFlowers([1,0,0,0,1], 2))
