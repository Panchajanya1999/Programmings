# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors
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
