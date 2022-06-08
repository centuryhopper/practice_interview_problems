


class MyHashMap:
    """
        This HashMap is implemented with the separate chaining technique
        Both keys and values must be non-negative
    """
    def __init__(self):
        # a list of list of key-value pairs
        # larger prime number for efficiency
        self.primeNum = 997

        # this will create 997 separate lists
        # as opposed to "[[]] * self.primeNum" which would give
        # each of those inner lists the same reference, which is bad!!!
        self.lst = [[] for _ in range(self.primeNum)]

    # given a key, this function
    # will map the value to the correct index
    def hashFunc(self, key: int) -> int:
        return (2*key + 1) % self.primeNum

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ind = self.hashFunc(key)
        hashedInnerLst = self.lst[ind]

        # if tuple found, update its value
        # otherwise append a new tuple
        for idx, (k, v) in enumerate(hashedInnerLst):
            if k == key:
                hashedInnerLst[idx] = (k, value)
                return
        hashedInnerLst.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        # go to the hashed inner list and find the key value pair
        # otherwise return -1
        ind = self.hashFunc(key)
        hashedInnerLst = self.lst[ind]
        # print(key, hashedInnerLst)
        for k, v in hashedInnerLst:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ind = self.hashFunc(key)
        hashedInnerLst = self.lst[ind]
        for idx, (k, v) in enumerate(hashedInnerLst):
            if k == key:
                # create a new tuple with the same
                # key and a new value because tuples are
                # immutable in python
                hashedInnerLst[idx] = (k, -1)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
