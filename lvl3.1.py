def solution(x, y,counter=None):
    counter=0 if counter is None else counter
    x=int(x)
    y=int(y)
    if y==x and y>1:
        return 'impossible'
    elif y>x:
        dif=y//x
        if y-x*dif>0:
            counter+=dif
            return solution(x,y-x*dif,counter)
        else:
            counter+=dif-1
            return solution(x,y-x*(dif-1),counter)
    elif y<x:
        dif=x//y
        if x-y*dif>0:
            counter+=dif
            return solution (x-y*dif,y,counter)
        else:
            counter+=dif-1
            return solution(x-y*(dif-1),y,counter)
    if y==x==1:
        return str(counter)
    
def solution1(x, y,counter=None):
    counter=0 if counter is None else counter
    if y==x and y>1:
        return 'impossible'
    elif y>x:
        counter+=1
        return solution(x,y-x,counter)
    elif y<x:
        counter+=1
        return solution (x-y,y,counter)
    if y==x==1:
        return str(counter) 
        