# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []

        for ch in s:
            if ch!="#":
                s1.append(ch)
            elif len(s1)>0:
                s1.pop()

        for ch in t:
            if ch!="#":
                t1.append(ch)
            elif len(t1)>0:
                t1.pop()
            
        return s1==t1