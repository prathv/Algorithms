from heapq import *

def find(l,x,k):
	close = _find(l,x,k)
	print close
def _find(l,x,k):
		pq = []
		c = []
		for i in range(len(l)):
			heappush(pq,(abs(l[i]-x),a[i],i))
	
		d = nsmallest(k,pq)
		e = nsmallest(k,d,key=lambda s: s[2]) 
		
		for i in range(len(e)):
			c.append(e[i][1])	
		return c
a = [4,1,3,2,7,4]
find(a,5.2,2)	
