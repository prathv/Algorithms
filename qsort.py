def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >=pivot]
		return [sort(left)] + [pivot] + [sort(right)]

def sorted(t,level=0):
	if t==[]:
		return []
	left, root, right = t
	return sorted(left,level+1)+[root]+sorted(right, level +1)

def _search(t,s):
	if t == []:
		return [] 
	left, root, right = t
	if (root == s):
		return t 
 	return _search(left,s)+_search(right,s)

def search(t,s):
	t = _search(t,s)
	if(t==[]):
		return False
	else:
		return True

def insert(t,s):
	left,root,right = t
	if(root == []):
		root = s
		return root
	else:
		if root < s:
			if right == []:
				right.append(s)
				
			else:
				insert(right,s)
		else:
			if left == []:
				left.append(s)
				
			else:
				insert(left,s)
	
	print(t)
	
		

	 
t = sort([4,2,6,3,5,7,1,9])


print t
print("Sorted output is ",sorted(t))
print("Search value for key == 2 is",search(t,2))
print("Tree after inserting 10 is")
insert(t,10)
