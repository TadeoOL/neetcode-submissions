class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dictS = {}
        dictT = {}

        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i]+= 1
        for i in t:
            if i not in dictT:
                dictT[i] = 1
            else:
                dictT[i]+= 1
        
        for letter, value in dictS.items():
            if letter not in dictT:
                return False
            if dictT[letter] != value:
                return False
        return True 