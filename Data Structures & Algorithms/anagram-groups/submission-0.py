class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}
        for s in strs:
            srt = "".join(sorted(s))
            if srt in group:
                group[srt].append(s)
            else:
                group[srt] = [s] 
            
        return list(group.values())
