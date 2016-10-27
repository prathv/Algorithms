from heapq import *
def ksmallest(k,a):
	result = []
	if type(a)== xrange:
		p = 0
		for i in a:
			if p == k:
				break
			else:
 				result.append(-i)
				p += 1
		if k > len(a):
			return "cannot return elements greater than size of input list"
	else:
		if k > len(a):
			return "cannot return elements greater than size of list"
	
		for i in range(k):
			result.append(-a[i])
	
	heapify(result)
	final = small(a,result,k)
	
	for i in range(k):
		final[i] = -final[i]
	
	return sorted(final)

def small(a,result,k):
	
	if len(a) == k :
		return result
		
	if -a[k] > result[0]:
		heappushpop(result,-a[k])
	k += 1
	return small(a,result,k)


	
				
a = [10, 2, 9, 3, 8, 11, 5]
print "Normal list is ", a
print " k smallest is",ksmallest(4,a)
print 
print "xrange list is ",xrange(1000,0,-1)
print "ksmallest is ",ksmallest(3,xrange(10000,0,-1))
