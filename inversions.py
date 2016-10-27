count = 0
def num_inversions(l):
	global count
	count = 0
	merge_sort(l)
	print(count)
def merge_sort(l):

    if len(l) < 2: return l 
    m = len(l) / 2 
    return  merge(merge_sort(l[:m]),merge_sort(l[m:])) 


def merge(l, r):
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result


