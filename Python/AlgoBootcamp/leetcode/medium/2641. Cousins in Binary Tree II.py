# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Return the root of the modified tree.
#
# Note that the depth of a node is the number of edges in the path from the root node to it.
#
#
#
# Example 1:
#
#
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
# Example 2:
#
#
# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 104
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
        q = deque([root])
        while q:
            curSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(curSum)
        level = 0
        q = deque([root])
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                levelSum = sums[level] if level < len(sums) else 0
                if node.left:
                    levelSum -= node.left.val
                if node.right:
                    levelSum -= node.right.val
                if node.left:
                    node.left.val = levelSum
                    q.append(node.left)
                if node.right:
                    node.right.val = levelSum
                    q.append(node.right)

        root.val = 0
        return root
