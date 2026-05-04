class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_index = self.hash(key)

        if hash_index not in self.collection:
            self.collection[hash_index] = {}

        self.collection[hash_index][key] = value

    def remove(self, key):
        hash_index = self.hash(key)

        if hash_index in self.collection and key in self.collection[hash_index]:
            del self.collection[hash_index][key]

            if not self.collection[hash_index]:
                del self.collection[hash_index]
    
    def lookup(self, key):
        hash_index = self.hash(key)
        bucket = self.collection.get(hash_index)

        if bucket and key in bucket:
            return bucket[key]
        
        return 

hash_table = HashTable()
print(hash_table.hash('golf'))
hash_table.add('golf', 'sport')

hash_table.add('dear', 'friend')
hash_table.add('read', 'book')

#hash_table.remove('golf')
print(hash_table.lookup('golf'))

hash_table.add('fcc', 'coding')
hash_table.add('cfc', 'chemical')
hash_table.add('rose', 'flower')

print(hash_table.collection)