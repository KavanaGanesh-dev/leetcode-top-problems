# https://leetcode.com/problems/zigzag-conversion/description/
'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000'''

# Some understanding from the question
# First how the letters are zigzagged - if I am able to understand this - then i have solved the problem.
# There are 2 inputs - string and the number os rows -  i need to rearrange the characters based on the rows
# First i need to identify the beginning and ending of the row: so i keep row pointer
# The moment i reach the row pointer = 0, i need to move downwards - so i keep direction = +1
# The momemt i reach the row_pointer = max row , i need to move upwards-so i keep the direction = -1
# I create the an empty string for each row - at each row - I start to concatenate the characters
# finally then join the characters
# create a list of num of row given. - ex:of numrows = 4
# then my list should looks like this = ["", "", "", ""]- finally use the join method
# "" -> this represent he bucket for row=0, row1, row2, row3

# Complexity analysis
# Time:I am traversing the entire string for each character at once  - therefore O(n)
# Space: Here I am storing the each character at once in the rows bucket - so O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        result = [""] * numRows
        row_count = 0
        direction = 1

        for char in s:
            result[row_count] = result[row_count] + char
            if row_count == 0:
                direction = 1
            elif row_count == numRows -1:
                direction = -1
            row_count = row_count + direction
        return "".join(result)
    
s = "A"
numRows = 1
print(Solution().convert(s,numRows))