
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

#--------------------------------------------------------
# December, 6th. Populating Next Right Pointers in Each Node II
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution_6(object):
    def find_node_by_map(self, root, tree_map):
        """Function that finds a node for a specific tree_map or returns none if it does not exist.
        Tree map is a string containing 1s and 0s and describing the path for getting from the root
        to a node. 1 for each right and 0 for each left."""
        current = root
        for path in range(1, len(str(tree_map))):
            if current is None:
                return None
            if str(tree_map)[path] == '0':
                current = current.left
            if str(tree_map)[path] == '1':
                current = current.right
        return current

    def next_map(self, tree_map):
        """Function that, given a tree_map, returns the map for the next node if the tree was full"""
        map_int = bin(int(tree_map, 2) + 1)
        map_str = str(map_int)
        return map_str[2:]

    def set_next_node_v1(self, root, current, parent, am_i_left, tree_map):
        """Function that sets the next node for each node in the tree.
        It uses next_map (in a loop) to get the theorical next node and then find_node_by_map
        to see if it exists and update current.next.
        This version of the solution worked, but the performance was too poor since it had to traverse
        the tree several times for each node."""
        if current is None:
            return
        if len(tree_map) > 1:
            if am_i_left and not(parent.right is None):
                current.next = parent.right
            else:
                next_node = None
                next_try = self.next_map(tree_map)
                while next_node is None and len(next_try) == len(tree_map):
                    next_node = self.find_node_by_map(root, next_try)
                    next_try = self.next_map(next_try)
                current.next = next_node
        self.set_next_node_v1(root, current.left, current, True, tree_map + '0')
        self.set_next_node_v1(root, current.right, current, False, tree_map + '1')

    def set_next_node(self, current, parent):
        """Function that sets the next node to the right for each node in the tree.
        It builds over the fact that, if we start always by the right leaf, the parent of every
        node must already have a next node defined when we search for the current next."""
        if current is None:
            return
        if not(parent is None):
            if not(parent.right is None) and parent.right != current:
                current.next = parent.right
            else:
                next_node = None
                parent_level = parent.next
                while next_node is None and not(parent_level is None):
                    if not(parent_level.left is None):
                        next_node = parent_level.left
                    else:
                        next_node = parent_level.right
                    parent_level = parent_level.next
                current.next = next_node
        self.set_next_node(current.right, current)
        self.set_next_node(current.left, current)


    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # self.set_next_node(root, root, root, False, '1') v1
        self.set_next_node(root, None)
        return root

# test_root = Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6, None, Node(8, Node(7), Node(9))))
# sol = Solution()
# original = sol.find_node_by_map(test_root, '1111')
# print(original.val)
# print(sol.set_next_node(test_root, original, '1111').val)

class Solution_7:
    def add_next(self, value, current_i, current_j, current_direction, spiral_matrix):
        """
        :type value: int - The value to be added to the matrix.
        :type current_i: int - The previous vertical position in which a value was added.
        :type current_j: int - The previous horizontal position in which a value was added.
        :type current_direction: int - value from 0 to 3 represents the current direction of the
         additions to the matrix (right, down, left, up)
        :type spiral_matrix: List[List[int]] - the matrix to be filled
        Function that adds the next value to spiral_matrix. If a value can be added in the next position
        according to current_direction, it is added. If not, the direction is updated and the function
        called again recursively with the new direction."""
        if current_direction == 0:
            if len(spiral_matrix[0]) > current_j + 1 and spiral_matrix[current_i][current_j + 1] == 0:
                spiral_matrix[current_i][current_j + 1] = value
                return current_i, current_j + 1, current_direction, spiral_matrix
        if current_direction == 1:
            if len(spiral_matrix) > current_i + 1 and spiral_matrix[current_i + 1][current_j] == 0:
                spiral_matrix[current_i + 1][current_j] = value
                return current_i + 1, current_j, current_direction, spiral_matrix
        if current_direction == 2:
            if current_j > 0 and spiral_matrix[current_i][current_j - 1] == 0:
                spiral_matrix[current_i][current_j - 1] = value
                return current_i, current_j - 1, current_direction, spiral_matrix
        if current_direction == 3:
            if current_i > 0 and spiral_matrix[current_i - 1][current_j] == 0:
                spiral_matrix[current_i - 1][current_j] = value
                return current_i - 1, current_j, current_direction, spiral_matrix
        current_direction = (current_direction + 1) % 4
        return self.add_next(value, current_i, current_j, current_direction, spiral_matrix)

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        Function that generates the empty matrix and, for every element in n**2, calls next_elem.
        """
        spiral_matrix = [[0 for i in range(n)] for j in range(n)]
        limit = n**2
        i = 0
        j = -1 # Because add_next will begin by adding 1 to j.
        direction = 0
        for next_elem in range(1, limit + 1):
            i, j, direction, spiral_matrix = self.add_next(next_elem, i, j, direction, spiral_matrix)
        return spiral_matrix

sol = Solution_7()
print(sol.generateMatrix(3))