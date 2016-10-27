def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1:] if x >=pivot]
		return [sort(left)] + [pivot] + [sort(right)]


def maxdepth(root):
	if(root == []):
		return 0
	else:
		left,root,right = root
		ldepth =maxdepth(left)
		rdepth =maxdepth(right)
		if(ldepth>rdepth):
			return ldepth+1
		else:
			return rdepth+1

def _longestpath(A):
	if(A==[]):
		return 0
	else:
		left,root,right = A
	ldepth = maxdepth(left)
	rdepth = maxdepth(right)
	
	lLongpath = _longestpath(left)
	rLongpath = _longestpath(right)

	return max(ldepth+rdepth, max(lLongpath, rLongpath))

def longest(A):
	path = _longestpath(A)
	print(path)
A = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]		

B = [[[],1,[]],2,[[],3,[]]]

