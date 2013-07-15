import sympy as sp


F_RANGE = 1000  # range of the components
delta = 0.5  # resolution parameter


x = sp.Symbol('x')


def h(m):
    flips = [sp.S("1")*j/(2*m) for j in range(2*m+1)]
    tk = []
    sign = sp.S("1")
    for i in range(2*m):
        tk.append((sign,(x,flips[i],flips[i+1])))
        sign = -1*sign
    return tk


def test1(interval):
    return [(sp.S("1"),(x,interval[0],interval[1]))]



def l2(a1,a2):
    prod = []
    for v, intrvl in a1:
        # checking for left overlap
        lefter = lambda l:l[1][1] < intrvl[1] and l[1][2] <= intrvl[2] and l[1][2] > intrvl[1]
        od = filter(lefter,a2)
        for left in od:
            prod.append([(left[0]*v,(x,intrvl[1],left[1][2]))])
        # checking for inner intervals
        inner = lambda l:l[1][1] >= intrvl[1] and l[1][2] <= intrvl[2]
        od = filter(inner,a2)
        for left in od:
            prod.append([(left[0]*v,(x,left[1][1],left[1][2]))])
        # checking for right overlap
        righter = lambda l:l[1][1] >= intrvl[1] and l[1][1] < intrvl[2] and l[1][2] > intrvl[2]
        od = filter(righter,a2)
        for left in od:
            prod.append([(left[0]*v,(x,left[1][1],intrvl[2]))])
        # checking for embedder intervals
        embedder = lambda l:l[1][1] < intrvl[1] and l[1][2] > intrvl[2]
        od = filter(embedder,a2)
        for left in od:
            prod.append([(left[0]*v,(x,intrvl[1],intrvl[2]))])
    return prod


a1 = test1((sp.S("1/2"),sp.S("1")))
a2 = test1((sp.S("2/3"),sp.S("2")))
print a1
print a2
print l2(a1,a2)
