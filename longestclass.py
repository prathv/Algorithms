
def _longest(tree):
    print tree
    if tree == []:
        return 0, 0
    Dleft, Mleft = _longest(tree[0])
    Dright, Mright = _longest(tree[2])
    return max(Dleft, Dright)+1, max(Mleft, Mright, Dleft+Dright)

def longest(tree):
    return _longest(tree)[1]


B = [[[],1,[]],2,[[],3,[]]]
print longest(B)
