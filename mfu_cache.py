from cache import Cache
from heapq import heapify, heappush, heappop

class heapNode():
    def __init__(self, freq, file):
        self.freq = freq
        self.file = file

    def __lt__(self, nxt):
        return self.freq > nxt.freq


class MFUCache(Cache):
    def __init__(self, cache_capacity):
        super().__init__(cache_capacity)
        self.cache = []

    def remove(self):
        return heappop(self.cache)

    def insert(self, file):
        while(not self.can_add(file.file_size)):
            popped_item = self.remove()
            self.update_memory(-1*popped_item.file.file_size)
            
        heappush(self.cache, heapNode(1, file))
        self.update_memory(file.file_size)

    def find(self, file):
        for ix, _cache_obj in enumerate(self.cache):
            if file.id == _cache_obj.file.id:
                self.cache[ix] = heapNode(self.cache[ix].freq +1, self.cache[ix].file)
                heapify(self.cache)
                return True
        return False

