
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

#--------------------------------------------------------
# December, 7th. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

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

#--------------------------------------------------------
# December, 8th. Pairs of Songs With Total Durations Divisible by 60
# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

class Solution_8:
    def numPairsDivisibleBy60(self, time_list):
        """
        :type time_list: List[int]
        :rtype: int
        Function that calculates the number of pairs of songs whose durations add up to something divisible by 60.
        It first stores the residue of 60 of every song in an list of len 60. And then multiplies each pairs of i, j
        such that i + j % 60 is cero.
        """
        durations_in_module = [0 for duration in range(60)]
        for song in time_list:
            durations_in_module[song % 60] += 1
        success_combinations = 0
        for i in range(60):
            for j in range(60):
                if (i + j) % 60 == 0:
                    success_combinations += durations_in_module[i] * durations_in_module[j]
                    if i == j:
                        success_combinations -= durations_in_module[i]
        return success_combinations/2


# sol = Solution_8()
# time_list = [30,20,150,100,40]
# print(sol.numPairsDivisibleBy60(time_list))

#--------------------------------------------------------
# December, 9th. Binary Search Tree Iterator.
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    """Implements an iterator using python's built in generator objects. Since python does not provide a
    hasNext method, the iterator counts the number of available nodes and updates the count in every yield
    as to provide the hasNext functionality"""
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.counter = 0
        self.total_length = 0
        self.count_length(root)
        self.inner_generator = self.inner_next(self.root)

    def count_length(self, current):
        if not(current is None):
            self.total_length += 1
            self.count_length(current.left)
            self.count_length(current.right)

    def next(self):
        """
        :rtype: int
        """
        self.counter += 1
        return next(self.inner_generator).val

    def inner_next(self, current):
        if not(current is None):
            yield from self.inner_next(current.left)
            yield current
            yield from self.inner_next(current.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.counter < self.total_length

# test_root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
# test_iter = BSTIterator(test_root)
# print(test_iter.next())
# print(test_iter.hasNext())

#--------------------------------------------------------
# December, 10th. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < A[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution_10(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        reached_peak = False
        for index in range(1, len(arr)):
            if not reached_peak:
                if arr[index] == arr[index-1]:
                    return False
                if arr[index] < arr[index-1]:
                    reached_peak = True
            else:
                if arr[index] >= arr[index-1]:
                    return False
        return reached_peak

# sol = Solution_10()
# print(sol.validMountainArray([1,3,2]))

#--------------------------------------------------------
# December, 11th. Remove Duplicates from Sorted Array II
# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Function that iterates over the array deleting the elemnts repeated more than twice.
        """
        if len(nums) >= 3:
            index = 2
            while index < len(nums):
                if nums[index] == nums[index - 2]:
                    del nums[index]
                else:
                    index += 1 # Only increases when element is not deleted.
        return len(nums)

#--------------------------------------------------------
# December, 12th. Smallest Subtree with all the Deepest Nodes
# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
# A node is called the deepest if it has the largest depth possible among any node in the entire tree.
# The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_12(object):
    def __init__(self):
        self.deepest_nodes = [[]] # So that it always has an element in index 0 to compare.

    def findDeepestNodes(self, current, path_to_current):
        """
        :type current: TreeNode
        :type path_to_current: List[int]
        Function that traverses the tree and adds to self.deepest_nodes all the pahts to the nodes with the highest depth
        """
        if current is None:
            return
        if len(self.deepest_nodes[0]) == len(path_to_current):
            self.deepest_nodes.append(path_to_current)
        elif len(self.deepest_nodes[0]) < len(path_to_current):
            self.deepest_nodes = [path_to_current]
        self.findDeepestNodes(current.left, path_to_current + [0])
        self.findDeepestNodes(current.right, path_to_current + [1])

    def findCommonAncestor(self):
        """
        Function that returns a path to the common ancestor of all elements in self.deepest_nodes
        """
        path_to_ancestor = []
        for level in range(len(self.deepest_nodes[0])):
            nodes = [self.deepest_nodes[k][level] for k in range(len(self.deepest_nodes))]
            if len(set(nodes)) == 1:
                path_to_ancestor.append(nodes[0])
            else:
                break
        return path_to_ancestor

    def findNodeByPath(self, root, path):
        """
        :type root: TreeNode
        :type path: List[int]
        :rtype: Treenode
        Function that raturns the reference to the node that can be found following the given path in the tree
        """
        del path[0] # Because the first element in path is always 1.
        current = root
        for turn in path:
            if turn == 0:
                current = current.left
            else:
                current = current.right
        return current

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Function that finds and returns te common ancestor to all the deepest nodes in the tree.
        """
        self.findDeepestNodes(root, [1])
        path_to_ancestor = self.findCommonAncestor()
        return self.findNodeByPath(root, path_to_ancestor)



test_root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
sol = Solution_12()
print(sol.subtreeWithAllDeepest(test_root).val)
print(sol.deepest_nodes)