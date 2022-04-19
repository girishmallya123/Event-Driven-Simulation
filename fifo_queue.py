from cache import Cache

class FifoQueue(Cache):
    def __init__(self, cache_capacity):
        super().__init__(cache_capacity)
        self.cache = []

    def remove(self):
        self.cache.pop(0)

    def insert(self, file):
        if self.can_add(file.file_size):
            self.cache.append(file)
            self.update_memory(file.file_size)
        else:
            while(not self.can_add(file.file_size)):
                to_remove = self.cache[0]
                self.update_memory(-1*to_remove.file_size)
                self.remove()

    def find(self, file):
        for _f in self.cache:
            if file.id == _f.id:
                return True
        return False

