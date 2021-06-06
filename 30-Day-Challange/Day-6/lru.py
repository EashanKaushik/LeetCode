class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.recently_used = list()
        self.current_capacity = 0


    def get(self, key):
        print('get ->', key)


        if key in self.cache:

            self.recently_used.remove(key)
            self.recently_used.insert(0, key)

            print(self.recently_used)

            print(self.cache[key])
            return
            # return self.cache[key]

        print(-1)
        # return -1

    def put(self, key, value):
        print('put ->', key, value)

        if key in self.cache:
            self.cache[key] = value
        else:

            if self.current_capacity < self.capacity:

                self.cache[key] = value
                self.recently_used.append(key)
                self.current_capacity += 1
            else:

                del(self.cache[self.recently_used.pop()])
                self.cache[key] = value
                self.recently_used.insert(0, key)

        print(self.cache)
        print(self.recently_used)


lRUCache =  LRUCache(2);
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)
