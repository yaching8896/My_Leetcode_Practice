class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for ids, idt in zip(s, t):
            if s.index(ids) != t.index(idt):
                return False
        return True