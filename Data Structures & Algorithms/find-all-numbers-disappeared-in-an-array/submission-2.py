class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        result = []
        nth = len(sortednums) + 1
        for s in sortednums:
            if s + 1 not in sortednums and s + 1 < nth:
                result.append(s + 1)
                sortednums.append(s + 1)
            else:
                continue
        for i in range(1, sortednums[0]):
            result.append(i)
        return result

        