def solution (h, q):
    N=0
    lis=[]
    for i in range(h):
        N+=2**i
    for node in q:
        if node>=(N):
            lis.append(-1)
        else:
            lis.append(traverse(h,N,node))
    return lis
                
def traverse(h,N,n):
    diff=test(h-1)
    if n==N or n==N-1:
        return n+1
    if n==N-1-diff:
        return n+diff+1
    elif n<N-1-diff:
        return traverse(h-1,N-1-diff,n)
    else:
        return traverse(h-1,N-1,n)
    
def test(n):
    c=1
    for i in range(n-1):
        c=c*2+1
    return c
