'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.'''

# few insights from understanding the problem
# 1.given input is string
# 2.split the string to remove the trailing and beginning extra spaces
# finally pick the last word and then find the length
# the key here is spliiting the string without passing anything in the method

# Compexity analsyis:
# Time: split() scans for each character to find the words : O(n)
# Space: once the split is sued; it creates a new string : O(n)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string = s.split()
        return len(split_string[-1])
    
s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))