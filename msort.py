def mergesort(A):
	sort = _mergesort(A)
	print(sort)
def _mergesort(A):
	if(len(A) <= 1):
		return [A[0]]

	mid = (len(A)/2)
	
	l = _mergesort(A[:mid])
	r = _mergesort(A[mid:])
	return merge(A,l,r)

def merge(A,l,r):
	i=0
	j=0
	k=0
	while i<len(l) and j<len(r):
		if l[i] < r[j]:
			A[k] = l[i]
			i+=1
		else:
			A[k] = r[j]
			j+=1
		k+=1
	while(i < len(l)):
		A[k] = l[i]
		k+=1
		i+=1
	while(j < len(r)):
		A[k] = r[j]
		j+=1
		k+=1
	return A

			
A=[2,3,1,4]
	
		
			
	
	 
