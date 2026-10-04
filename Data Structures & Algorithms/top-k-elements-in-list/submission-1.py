class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        i = 0
        for n in nums:
            
            if n in group:
                group[n] += 1
            else:
                group[n] = i + 1
        
        t = sorted(group, key=group.get, reverse=True)
        return t[:k]