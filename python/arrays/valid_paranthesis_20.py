'''iven a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false'''

# Things to keeo in mind:
# 1. if its open bracket - same type of close bracket
# 2 order matters while closing bracket
# My idea:
# 1. if char is open bracket- push to the stack
# 2. if its a closing bracket - check it its a match? if a match pop it from the stack


# complexity analysis
# Time : push , pop and dict check is o(1) operation but it iterates through the lopp once- o(N)
# Space: dict takes o(1) : only 3 elements irrespective of the input. doesnot grow. stack is o(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hahsmap = {')': '(', 
                   '}': '{',
                   ']':'['}
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack or stack[-1] != hahsmap[char]: # if s = "()))" - if not stack comes into condition
                    return False
                stack.pop()

        return True if len(stack) == 0 else False

s = "([])"
print(Solution().isValid(s))
            