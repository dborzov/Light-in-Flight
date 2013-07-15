def component(m):
    flips = [x/float(m) + 1./float(2.*m) for x in range(m)] #
    return flips

def h(m):
    flips = [(x+1.)/float(2.*m) for x in range(2*m)] #
    return flips



def l2(n,m):
    conv = [0.] + sorted(component(m)+component(n)) + [1.]
    l2 = 0.
    sign = 1.
    for i,x in enumerate(conv[:-1]):
        l2 += sign*(conv[i+1] - conv[i])
        sign = -1.*sign
    return l2


def l2h(n,m):
    conv = [0.] + sorted(h(m) + h(n)) + [1.]
    l2 = 0.
    sign = 1.
    for i,x in enumerate(conv[:-1]):
        l2 += sign*(conv[i+1] - conv[i])
        sign = -1.*sign
    return l2


print l2(0,3)
print l2(0,3)
