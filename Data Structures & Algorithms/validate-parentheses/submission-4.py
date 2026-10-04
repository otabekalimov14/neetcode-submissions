class Solution:
    def isValid(self, s: str) -> bool:

        brackets = { ")" : "(", "]" : "[", "}":"{" }
        stack = []
        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if stack == []:
                    return False

                if brackets[b] == stack.pop():
                    continue
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

        