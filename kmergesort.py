from heapq import *
from math import ceil
def partition(lst,d):
	sublist = []
	if len(lst) == 1:
		return lst

	j = ceil(len(lst)/float(d))
	j = int(j)	
	for i in range(0,len(lst),j):
		sublist.append(lst[i:i+j])
	
	for i in range(len(sublist)):
		sublist[i] = sorted(sublist[i])
	
	a= []	
	j = 2
	
	return [a for a in merge(sublist[i])]

	

def kmerge(*lists):
	print lists
a = [1,3,4,2,5]   

print partition(a,3)
