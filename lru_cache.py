from cache import Cache
from collections import OrderedDict

class LRUCache(Cache):
    def __init__(self, cache_capacity):
        super().__init__(cache_capacity)
        self.cache = OrderedDict()
        
    def remove(self):
        return self.cache.popitem(last = False)

    def insert(self, file):
        while(not self.can_add(file.file_size)):
            popped_item = self.remove()
            self.update_memory(-1*popped_item[1].file_size)
            
        self.cache[file.id] = file
        self.cache.move_to_end(file.id)
        self.update_memory(file.file_size)

    def find(self, file):
        if file.id in self.cache:
            self.cache.move_to_end(file.id)
            return True
        return False
