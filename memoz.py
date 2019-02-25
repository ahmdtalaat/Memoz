class fibonacci:
    memo = []  # memoization list

    def __init__(self, n):  # initialize a list of n None values
        self.memo = [None]*(n+1)

    def check_index_range(self, n):  # if index out of range just add more None values
        if len(self.memo) <= n:
            bla = n - len(self.memo)+1
            for _ in range(bla):
                self.memo.append(None)

    def fib(self, n):  # Fibonacci function
        self.check_index_range(n)
        if n <= 0:
            self.memo[n] = 0
        elif n == 1:
            self.memo[n] = 1
        else:
            if not self.memo[n]:
                self.memo[n] = self.fib(n-1)+self.fib(n-2)
            else:
                return self.memo[n]
        return self.memo[n]
