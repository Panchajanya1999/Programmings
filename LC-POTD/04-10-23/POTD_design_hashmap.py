# POTD October 4, 2023
# Design HashMap
# Link - https://leetcode.com/problems/design-hashmap/description/ 

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Value shouldn't exceed 10 ** 6
        # Initialize with -1
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        """
        Puts the key and value in the HashMap
        """
        self.data[key] = value

    def get(self, key: int) -> int:
        """
        Gets the value from a given key
        """
        _val = self.data[key]
        if _val is None:
            return -1
        else:
            return _val

    def remove(self, key: int) -> None:
        """
        Removes a value from a given key
        """
        self.data[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)