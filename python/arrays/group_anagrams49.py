'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.'''

# Problem analysis:
# 1. when is the anagran : string that have same frequency of characters but theor order may vary
# 2. Do you think - I should mainatain frequency ? not required: instead i will just sort the string and use that as the key
# 3. Prepare the hashmap.
# 4. iterate through each string sort the string  (Remember the output of the sort is list datatype: we cannot use list as key within the dictionary)
# 5. check if the string is present as a key, if yes append the value to that key
# 6. create another key and append the element picked as an value
# 7. finally return only the values as a list


# Compelxity Analysis
# Time: I am iterating through each element (O(n))in the list and each element has size k. and then sorted O(klogk). 
    # Total = O(n* klogk) = O(nk)
# Space: Storing the entire list and key(this is sorted one) = O(nk)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            sorted_key = "".join(sorted(str))
            if sorted_key in hashmap:
                hashmap[sorted_key].append(str)
            else:
                hashmap[sorted_key] = [str]

        return list(hashmap.values())
                

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))