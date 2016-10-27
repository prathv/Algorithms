from math import *
from numpy import *


def max_wis(lst,cache = None):
	if cache == None:
		cache = {}
	maxl = []
	i = len(lst) - 1
	cache[i+1] = 0
	cache[i+2] = 0
	while i >= 0:
		cache[i] = max(lst[i] + cache[i+2],cache[i+1])
				
				
		i-=1
	n = 0 

	while n <len(lst): 
		if cache[n+1] >= cache[n+2] + lst[n]:
			n = n+1
		else:
			maxl.append(lst[n])
			n = n+2

	return cache[0],maxl
					
		
def max_wis2(lst,cache = None):
	if cache == None:
		cache = {}
	maxl = []
	i = 0
	cache[-1] = 0
	cache[-2] = 0 	
	
	while i < len(lst):
		cache[i] = max(lst[i]+cache[i-2],cache[i-1])
		i += 1
	
	n = len(lst) - 1

	while n >= 0:
		if cache[n-1] >= cache[n-2]+lst[n]:
			n = n-1
		else:
			maxl.append(lst[n])
			n=n-2
	return cache[len(lst)-1],maxl

	

		
		

		

a = [5,8,7]
# a = [10,9,8,7]
# a = [-1,-2,-3]
# a = [-1,10.20]

#print(max_wis(a))





