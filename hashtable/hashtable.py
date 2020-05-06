class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_head(self, key, value):
        node = HashTableEntry(key, value)
        node.next = self.head
        self.head = node

    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next

        return None

    def append_at_tail(self, key, value):
        node = HashTableEntry(key, value)

        if head is None:
            self.head = node
            return
        
        cur = self.head
        while cur is not None:
            cur = cur.next
        
        cur.next = node

    def delete(self, key):
        cur = self.head

        if cur.key == key:
            self.head = self.head.next
            cur.next = None
            return cur

        prev = None

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
            prev = cur
            cur = cur.next

        return None
        
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = max(capacity, 8)
        self.storage = [None] * self.capacity
        self.size = 0
        
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        h = 14695981039346656037
        for b in str(key).encode():
            h ^= b
            h *= 1099511628211
        return h

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)
        if self.storage[index] is None:
            self.storage[index] = LinkedList()
            self.storage[index].add_to_head(key, value)
        else:
            n = self.storage[index].find(key)
            if n is None:
                self.storage[index].add_to_head(key, value)
            else:
                n.value = value
        self.size += 1
        if self.load() > 0.7:
            self.resize()
    
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        n = self.storage[index].find(key)
        self.storage[index].delete(key)
        if n is not None:    
            self.size -= 1
        if self.load() < 0.2:
            self.resize(0.5)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None or self.storage[index].find(key) is None:
            return None
        else:
            return self.storage[index].find(key).value

    def resize(self, resize_factor=2):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        old = self.storage
        self.capacity = max(self.capacity*resize_factor, 8)

        self.storage = [None] * self.capacity
        for entry in old:
            if entry==None: continue
            else:
                cur = entry.head
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next

    def load(self):
        return self.size/self.capacity

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
