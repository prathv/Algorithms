					
def find(a,x,k):
	a = sorted(a)
	return closest(a,x,k)

def _find(l,x,low,high):
	if(l[high] <= x):
		return high
	
	if(l[low]>x):
		return low
	
	mid = (low+high)/2
	
	if(l[mid] <= x and l[mid+1] > x):
		return mid

	if (l[mid]< x):
		return _find(l,x,mid+1,high)

	return _find(l,x,low,mid-1)

def closest(a,x,k):
	if a == []:
		return "No List input given"
	l = _find(a,x,0,len(a)-1)
	r = l+1
	count = 0
	close = []

	while(l>=0 and r< len(a) and count<k):
		if(abs(x-a[l]) <= abs(a[r]-x)):
			close.insert(0,a[l])
			l -= 1
		else:
			close.append(a[r])
			r += 1
		count += 1
	
	while(count < k and l>=0):
		close.insert(0,a[l])
		l -= 1
		count += 1
	
	while(count < k and r < len(a)):
		close.append(a[r])
		r += 1
		count += 1

	return close
		
# TEST CASES	
import random
print("\n")
a= []
print "list is",a
print find([],2,1)
print("\n")

lst = range(10)
x = random.uniform(1,10)
c = random.randint(1,10)
random.shuffle(lst)
lst = sorted(lst)
print "list is",lst
print "query is",x
print "count is",c

print find(lst,x,c)

print("\n")

lst = range(8)
x = random.randrange(1,8)
c = random.randint(1,8)
random.shuffle(lst)
lst = sorted(lst)

print "list is",lst
print "query is",x
print "count is",c
print find(lst,x,c)


	
