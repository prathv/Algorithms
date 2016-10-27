from math import *
import numpy


def max_wis(lst,cache = None):
	if cache == None:
		cache = {}
	maxl = []
	i = len(lst) - 1
	cache[i+1] = 0
	cache[i+2] = 0
	while i > 0:
	
		if lst[i] + cache[i+2] > cache[i+1] or lst[i] > cache[i-1]:
			if a[i] > cache[i-1]:
				cache[i] = lst[i]
			else:
				cache[i] = lst[i] + cache[i-2]
			i += 1  
		else: 
			cache[i] = cache[i-1]
			i += 1	
		
	return cache[len(lst)-1],maxl
					
		
def max_wis2(lst = None):
	maxs = []
	lst = [float('-inf')] + lst
	lst = [float('-inf')] + lst
	a = qmaxpair(lst,0,maxs)	
	return 0
def maxpair(lst,final,maxs):
	print lst[len(lst)-1],final,maxs
	if len(lst) <= 1:
		print (final,maxs)
		return 0
	
	if lst[len(lst)-1] > lst[len(lst)-2] and final + lst[len(lst)-1] >= final:
				print "entered"
				maxs.append(lst[len(lst)-1])
				if lst[len(lst)-1] > final + lst[len(lst)-1]:
					return lst[len(lst)-1] + maxpair(lst[:len(lst)-2],lst[len(lst)-1],maxs)
				else:
					return lst[len(lst)-1] + final + maxpair(lst[:len(lst)-2],final + lst[len(lst)-1],maxs)
	else:
		return maxpair(lst[:len(lst)-1],final,maxs)
			

	

		
		

		

a = [-10,8,10]


print max_wis(a)

#max_wis2(a)





