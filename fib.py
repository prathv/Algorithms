import time
def fib2(n, cache=None):
                if cache is None:
                    cache = {}
                if n in cache:
                    return cache[n]
                cache[n] = 1 if n <= 2 else fib2(n-1, cache) + fib2(n-2, cache)
                return cache[n]

def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-2) + fib(n-1)

for i in range(5,35):
	start = time.time()	
	fib2(i)
	print i," ",'{0:05f}'.format(time.time()-start)
