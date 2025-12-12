'''981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.'''


# Insights after understanding the question
# 1. I need to return the value at the timestamp or value less than the timestamp
# 2. I need to select the DS to store key and value. But value has 2 entity: value 
# 3. I need to traverse the DS and look for numbers in ascending order: when I look  : O(n)
# 4. Something better than O(n) is O(logn). Since the data is already sorted for me : i use binary search - O(logn)

# Time complexity analysis
# set(): checking membership - O(1), then i do append to the list - O(1) . Therefore O(1)
# get(): Binary search has its own loop - O(logn)
# space complexity:
# I used dictionary to store the key: value pairs - O(N) - N is the number of timestamps


class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] =[]
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        result = " "
        values = self.hashmap[key]
        left, right = 0, len(values)-1
        
        while left <= right:
            mid = (left+right)//2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = left+1
            else:
                right = right-1
        
        return result
            
mp = TimeMap()
print(mp.set("foo", "bar", 1))
print(mp.get("foo", 1))
print(mp.get("foo", 3))
print(mp.set("foo", "bar2", 4))
print(mp.get("foo", 4))
print(mp.get("foo", 5))
        

