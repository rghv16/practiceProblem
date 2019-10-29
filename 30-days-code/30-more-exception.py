class Calculator:

    def power(self, n, p):
        from math import pow
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return int(pow(n, p))
