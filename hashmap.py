class HashMap:
    #constructor
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    #search O(1)
        #search based on the key
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        record__val, record_key = None
        for i, record in enumerate(bucket):
            record_key, record__val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record__val
        else:
            return "No record exists"
    #insert O(1); insert values into hashmap
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size()
        bucket = self.hash_table[hashed_key]
        found_key = False
        if self.get_val(key):
            found_key = True
            bucket[index] = (key,val)
        else:
            #if not found
            bucket.append((key, val))
    #remove O(1)
    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        if self.get_val(key):
            bucket.pop(index)
        else:
            #if not found
            return "No record found cannot be removed"