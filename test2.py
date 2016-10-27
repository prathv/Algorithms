
import math, random, time
def _qselect(k,a):  
    print k,a
    pindex = random.randint(0, len(a)-1)
    a[0], a[pindex] = a[pindex], a[0]
    pivot = a[0]
    print pivot
    left = [x for x in a if x < pivot]
    mid = [x for x in a[1:] if x == pivot]
    print "left is",left,mid
    lleft, lmid = len(left), len(mid)
    print "lleft is",lleft,"lmid is ",lmid
    if k <= lleft:
	print "entered 1"
        return _qselect(k, left)
    elif k <= lleft+lmid+1:
	print "entered 2"
        return pivot, lleft, k-lleft
    else:
	print "entered 3"
        right = [x for x in a[1:] if x > pivot]
        diff = lleft+1+lmid
        r0, r1, r2 = _qselect(k-diff, right)
        return r0, r1+diff, k-r1-diff

def find(lst, w, num):
    lst_abs = map(lambda x: round(math.fabs(x-w), 10), lst)
    maxdiff, num_small, rest = _qselect(num, list(lst_abs))
    print "maxdiff is",maxdiff,"num_small is",num_small,"resit is",rest
    result = []
    i = 0
    while rest > 0 or num_small > 0:
        if lst_abs[i] < maxdiff and num_small > 0:
	    print "entered 1 in find",rest,num_small
            result.append(lst[i])
            num_small -= 1
        elif lst_abs[i] == maxdiff and rest > 0:
	    print "entered 2 in find",rest
            result.append(lst[i])
            rest -= 1
        i += 1
    return result


print find([4,1,3,2,7,4], 5.2, 2)
