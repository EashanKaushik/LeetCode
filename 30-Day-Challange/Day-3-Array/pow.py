class Solution:
    def myPow(self, x, n):
        value = 1

        if n == 0:
            return 1

        if n > 0:

            while n >= 1:

                value = value * x
                n -= 1

        else:
            x = 1 / x

            while abs(n) >= 1:
                value = value * x
                n-= 1


        return value

    def myPow2(self, x, n):
        negative = False

        value = 1
        
        if n == 0:
            return 1

        if n < 0:
            n = abs(n)
            negative = True

        while n >= 1:

            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                value *= x
                n -= 1

        return (1/value) if negative else value


s = Solution()

print(s.myPow(2.10000, 3))
