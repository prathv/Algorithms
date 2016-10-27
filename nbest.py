import itertools

def nbesta(a,b):
	lst = []
	for x,y in itertools.product(a,b):
    		lst.append((x,y))
	
	for i in range(len(lst)):
		for j in range(i+1,len(lst)):
			if ((lst[j][0] + lst[j][1]) < (lst[i][0] + lst[i][1])):
				lst[i],lst[j] = lst[j],lst[i]
			elif((lst[j][0] + lst[j][1]) == (lst[i][0] + lst[i][1]) and lst[j][1] < lst[i][1]):
				lst[i],lst[j] = lst[j],lst[i]
			else:
				continue
	lst = lst[:4]
	return lst

		
a = [1,2,3,4]
b = [6,2,1,3]

print a 
print b
print "nbest solution is"
print nbesta(a,b)

