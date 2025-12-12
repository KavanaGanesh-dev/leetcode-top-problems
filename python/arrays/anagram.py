"""
Problem: To find the given two strings are anagram or not - Return True or False
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
https://neetcode.io/problems/is-anagram?list=neetcode150
Approach: Hashmap counter
Time: O(n)
Space: O(n)"""

from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_count = Counter(s)
        for c in t:
            if c not in s_count or s_count[c] == 0:
                return False
            s_count[c] = s_count[c] - 1
        return True
    
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))


