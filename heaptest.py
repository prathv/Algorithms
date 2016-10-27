from heapq import *
import time

def heaptest(a):
	result = []
	r = a
	print "time taken for insert heap is "
	start = time.time()
	for i in range(len(a)):
		heappush(result,a[i])
	end = time.time() - start
	print '{:.10f}'.format(end)



	b = a
	print "time taken fo heapify is"
	start = time.time()
	heapify(b)
	end = time.time()-start
	print '{:.10f}'.format(end)


	c = sorted(a)
	result = []
	print" for sorted list, time taken for insert heap is"
	start = time.time()
	for i in range(len(c)):
		heappush(result,c[i])
	end = time.time() - start
	print '{:.10f}'.format(end)



	print"for sorted list time taken for heapify is"
	start = time.time()
	heapify(c)
	end = time.time() - start
	print '{:.10f}'.format(end)


	
	
	sorted(r,reverse=True)
	result = []
	print"for reverse sorted list, time taken to insert is"
	start = time.time()
	for i in range(len(r)):
		heappush(result,r[i])
	end = time.time() - start
	print '{:.10f}'.format(end)



	print"for sorted list time taken for heapify is"
	start = time.time()
	heapify(r)
	end = time.time() - start
	print '{:.10f}'.format(end)

		
	








a = [ 2,3,1,4,6,0,5,10,11,9,8]
heaptest(a)
