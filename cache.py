from abc import ABC, abstractmethod

class Cache(ABC):
    def __init__(self, cache_capacity):
        self.cache_capacity = cache_capacity
        self.memory_consumed = 0

    def update_memory(self, memory):
        self.memory_consumed += memory

    def can_add(self, memory):
        return ((self.memory_consumed + memory) <= self.cache_capacity)

    @abstractmethod
    def insert(self, file):
        pass

    @abstractmethod
    def find(self, file):
        pass

    @abstractmethod
    def remove(self):
        pass
