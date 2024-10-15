# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = [root]
        average = [root.val]

        while level:
            queue, levelSum = [], 0
            for node in level:
                if node.left:
                    queue.append(node.left)
                    levelSum += node.left.val
                
                if node.right:
                    queue.append(node.right)
                    levelSum += node.right.val

            if queue:
                average.append(levelSum/len(queue))
            
            level = queue
            # print(level)
        return average

        