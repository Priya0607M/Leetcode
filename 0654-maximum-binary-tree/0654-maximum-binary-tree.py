# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_value = max(nums)
        i = nums.index(max_value)

        left_array = nums[:i]
        right_array = nums[i+1:]

        root = TreeNode(max_value)

        root.left = self.constructMaximumBinaryTree(left_array)
        root.right = self.constructMaximumBinaryTree(right_array)

        return root
        