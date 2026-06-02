class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test = []
        if len(s) != len(t):
            return False
        else:
            for i in s:
                test += [i]
            for i in t:
                if i in test:
                    test.remove(i)
            if test == []:
                return True
            else:
                return False
