def solution(l):
    n=len(l)
    graph=[[None]*n for _ in range(n)]
    n=len(l)
    for i in range(n):
        for j in range(n):
            if check(l[i],l[j])==True:
                graph[i][j]=check(l[i],l[j])
                graph[j][i]=graph[i][j]
    def pair(u, match, seen):#had to get help online for this
        for v in range(n):
            if graph[u][v] and seen[v] == False:
                seen[v] = True
                if match[v] == -1 or pair(match[v], match, seen):
                    match[v] = u
                    return True
        return False
    
    match=[-1] * n
    result=0
    for i in range(n):
        seen = [False]*n
        if pair(i,match,seen):
            result+=1
    return n-2*(result//2)
def gcd(x, y):
        if x < y:
            x, y = y, x
        while (y):
            x, y = y, x % y
        return x
def check(x,y):
    quotient = (x+y)/gcd(x, y)
    if int(quotient) != quotient:
        return True
    quotient = int(quotient)
    return (quotient & (quotient-1)) != 0  