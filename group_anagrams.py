'''
Problem: Given an array of strings strs, group all anagrams together into sublists -  Return is a lists of lists , order of the characters doesnot matter
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
https://leetcode.com/problems/group-anagrams/description/
Approach: Hahmap, each word mapping to the same key. Key will be the sorted string and value will be the list of original strign that matches the key
Time: 
Space: '''


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagram(self, strs:List[str])->List[List[str]]:
        new_dict = defaultdict(list)
        print(new_dict)

        for str in strs:
            new_key = "".join(sorted(str))
            print(new_dict)
            new_dict[new_key].append(str)
        return list(new_dict.values())
    


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# # strs = ["a"]
print(Solution().groupAnagram(strs))

