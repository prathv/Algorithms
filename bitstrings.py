def num_yes(n):
	binf = '{0:0'+str(n)+'b}'
	finalc = 0
	for i in range(0,(2*n)-1):
		binary = binf.format(i)
		count = 0
		d = 1
		j = 0
		while j < n:
			if binary[j] =='0':
				count += 1
			else:
				count = 0	
			if count >= 2:
				finalc += 1
				j = n
			j += 1
	return finalc 
				
		
def num_no(n):	
	binf = '{0:0'+str(n)+'b}'
	finalc = 0
	for i in range(0,(2*n)-1):
		binary = binf.format(i)
		count = 0
		d = 1
		j = 0
		while j < n:
			if binary[j] =='0':
				count += 1
			else:
			 	count = 0
				
			if count < 2:
				finalc += 1
				j = n
			j += 1
			
	return finalc 		
		
	
print num_no(3)
