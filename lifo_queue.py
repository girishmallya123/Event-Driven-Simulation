from cache import Cache

class LifoQueue(Cache):
    def __init__(self, cache_capacity):
        super().__init__(cache_capacity)
        self.cache = []

    def remove(self):
        self.cache.pop()

    def insert(self, file):
        while(not self.can_add(file.file_size)):
            to_remove = self.cache[-1]
            self.update_memory(-1*to_remove.file_size)
            self.remove()

        self.cache.append(file)
        self.update_memory(file.file_size)

    def find(self, file):
        for _f in self.cache:
            if file.id == _f.id:
                return True
        return False

