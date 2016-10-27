import random 


def qselect(i,A):
	return _qselect(A,0,len(A),i)

def _qselect(A,p,r,i):
	if p == r:
		return A[p]
	q,A=partition(A,p,r)	
	k = q-p+1
	if i == k:
		return A[q]
	elif i < k:
		return _qselect(A,p,q-1,i)
	else:
		return _qselect(A,q+1,r,i-k)



def partition(A,p,r):
	x = random.choice(A)
	y = A.index(x)
	left=[]
	right = []
	for i in range(len(A)):
		if(i == y):
			continue
		elif(A[i] <= x):
			left.append(A[i]) 
		else:
			right.append(A[i])
	A=left+[x]+right
	return A.index(x),A

A = []

print("Enter the size of the list")
s = input()

print("Enter the values for the list\n")
for i in range(s):
	p = input()
	A.append(p)

print("Now enter the ith smallest element to find\n")
i=input()
if i > len(A):
	print("Invalid ith index value")
else:
	print(qselect(i,A))
	
