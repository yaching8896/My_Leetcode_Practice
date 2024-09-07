class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist = {}

        for i, v in enumerate(nums):
            if v in dist and i - dist[v] <= k:
                return True
            dist[v] = i
        return False