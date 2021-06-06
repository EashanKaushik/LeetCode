from collections import deque

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.recently_used = deque()
        self.current_capacity = 0

    def get(self, key):
        print('get ->', key)


        if key in self.cache:

            self.recently_used.remove(key)
            self.recently_used.append(key)

            return self.cache[key]

        return -1

    def put(self, key, value):
        print('put ->', key, value)

        if key in self.cache:
            self.cache[key] = value
            self.recently_used.remove(key)
            self.recently_used.append(key)
        else:
            if self.current_capacity < self.capacity:

                self.cache[key] = value
                self.recently_used.append(key)
                self.current_capacity += 1
            else:
                del(self.cache[self.recently_used.popleft()])
                self.recently_used.append(key)
                self.cache[key] = value


lRUCache =  LRUCache(2);
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)
