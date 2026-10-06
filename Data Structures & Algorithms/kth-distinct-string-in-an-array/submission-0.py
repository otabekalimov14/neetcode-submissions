class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        sdict = {}
        tracker = k - 1
        for c in arr:
            if arr.count(c) > 1:
                continue
            elif c not in sdict:
                sdict[c] = 1

            else:
                sdict[c] += 1
        if len(sdict) < k:
            return ""
        result = list(sdict.keys())[tracker]

        return result
        