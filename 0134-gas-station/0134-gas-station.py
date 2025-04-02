class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return  -1

        remain = [i-j for i, j in zip(gas, cost)]
        
        start = num = 0
       
        for i, v in enumerate(remain):
            if num < v:
                start, num = i, v

        return start
        