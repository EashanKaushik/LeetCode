class Solution:
    def countPrimes(self, n: int):
        if n <= 2:
            return 0

        not_prime = set()

        for index in range(2, int(sqrt(n)) + 1):
            if index not in not_prime:
                for multiple in range(index * index, n, index):
                    not_prime.add(multiple)

        return n - len(not_prime) - 2
