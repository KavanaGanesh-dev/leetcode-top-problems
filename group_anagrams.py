'''
Problem: Given an array of strings strs, group all anagrams together into sublists -  Return is a lists of lists , order of the characters doesnot matter
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
https://leetcode.com/problems/group-anagrams/description/
Approach: Hahmap, each word mapping to the same key. Key will be the sorted string and value will be the list of original strign that matches the key
Time: O(N * KlogK). N = number of strings, K = max length of string. Sorting is O(KlogK) and dict insertion is O(1)
Space: O(N*K). we are storing all strings
'''


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagram(self, strs:List[str])->List[List[str]]:
        new_dict = defaultdict(list)

        for str in strs:
            new_key = "".join(sorted(str))
            new_dict[new_key].append(str)
        return list(new_dict.values())
    


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# # strs = ["a"]
print(Solution().groupAnagram(strs))

