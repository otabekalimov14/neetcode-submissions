class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tracker = 0
        best = 0
        for n in nums:
            if n == 1:
                tracker +=1
            else:
                best = max(tracker, best)
                tracker = 0
        return max(tracker, best)