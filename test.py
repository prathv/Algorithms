import bisect

def find(a, x, k):
    print a,x,k
    assert k <= len(a), "k shouldn't be larger than n!"
    a = [float("-inf")] + a + [float("inf")]
    print "after a is",a
    place = bisect.bisect(a, x)
    print "place is ",place
    i, j = place-1, place
    print "i and j is",i,j
    print "xrange is ",xrange(k)

    for _ in xrange(k):
        if x-a[i] <= a[j]-x:
	    print "entered 1"
            i -= 1
        else:
	    print "entered 2"
            j += 1
    return a[i+1:j]


print find([1,2,3,4,4,6,6], 5, 3)
