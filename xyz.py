g = []
def find(a):
	count = []
	a = sorted(a)
	for i in range(len(a)):
		count += _find(a,0,len(a)-1,a[i])
		i += 1
	return tuple(count) 

def _find(a, l, h ,i):
	
	if l == i:
		l += 1
	
	if h == i:
		h -= 1

	if (a[l]+a[h]) == i:
		return [[a[l],a[h],i]]

	if l == h:
		return []

	if(a[l] + a[h] > i):
		if(a[l] <=  a[h]):
			h -= 1
	elif(a[l] + a[h] < i):
			l += 1
	return [] +_find(a,l,h,i)
	
		
a = [1,2,3,4,5]
print find(a)
