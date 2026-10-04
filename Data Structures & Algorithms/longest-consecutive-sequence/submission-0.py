class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0
        for num in numset:
            length = 1
            if num - 1 in numset:
                continue
            while num + length in numset:
                length +=1
            else:
                best = max(length, best)
        return best