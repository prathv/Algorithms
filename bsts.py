memo = [0] * 10

def bsts(n):
	return subbst(a)


def subbst(n):
	global memo
	if n == 1 or n == 0:
		return 1

	left = 0
	right = 0
	sums = 0
	for i in range(1,n+1):
		if memo[i-1] == 0:
			memo[i-1] = subbst(i-1)
			

		left = memo[i - 1]
		if memo[(n-i)] == 0:
			memo[n-i] = subbst(n-i)
		
		right = memo[n-i]
		sums += (left*right)

	return sums	
	
a = 3
print bsts(a)
