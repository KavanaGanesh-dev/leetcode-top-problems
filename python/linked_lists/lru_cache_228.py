'''Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.'''

# few insights from the problem:
# 1.I will use hashmap for keu lookup - operations - O(n)
# 2. I use doubly linkedlist to add and remove - the operations are O(1)
    # why i used doubly linked list list - 
        # move the nodes to front  - to mark it as most recently used
        # evict the nodes from back -  tomark it as least recently used
        # both these operations are O(1)
# Complexity
# 1. Space - O(capacity)
# 2. Time - get and put operations are both O(1)


# There is a class Node :  a doubly linked list - prev, tail, key, value
# There is LRU cache class : capacity, hashmap, dummy head node, dummy tail node

# Complexity Analysis:
# 1. Time - get and put operations are both O(1)
# 2. Space - Stores in the hashmap of the size of capacity - O(capacity)


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # removing a node from doubly linkedlist list - operation O(1)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def _add_to_front(self, node):
        # [head] ←→ [A] ←→ [B]
        node.next = self.head.next # [head] ←→ [A] ←→ [B]: 'Node' pointing to A as well:
        node.prev = self.head # [head]<-Node->[A] ←→ [B]: But head.next still pointing to A and A.prev is still pointing to head
        self.head.next.prev = node #[head]<-Node<->[A] ←→ [B]
        self.head.next = node #[head]<->Node<->[A] ←→ [B]

    def _move_to_front(self, node):
        # here i make the node as the most recent node- most recently used will be deleted from the linkedlist
        self._remove(node) # this node couble be located anywhere in the linkedlist - i just remove it
        self._add_to_front(node) #now i put the removed node as the first element in the linkedlist making it as the most recently used

    def get(self, key: int) -> int:
        # check if key exists in the cache, if yes return value else return -1
        # if the key exists- do not forget to make that as the most recently used
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key:int , value:int):
        # if key and value exists - create a double linkedlist Node and make it as the most recently used
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
        # otherwise - always add the node irrespective of the size of the cache capacity
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            # if key doesnot exists then check for the capacity of the cache
            # make that as the lru node to evict from the linkedlist - finally delete from the cache
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

cache = LRU_cache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Returns 1
cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # Returns -1 (not found)
cache.put(4, 4)      # Evicts key 1
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3
print(cache.get(4))  # Returns 4