class Solution:
    def countSeniors(self, details: List[str]) -> int:
        tracker = 0
        
        for x in details:
            if int(x[11:13]) > 60:
                tracker += 1
        return tracker 

        