
def countPerm(n):
    a = e= i=o=u = 1

    for _ in range(n-1):
        a,e,i,o,u = e,a+i,a+e+o+u,i+u,a
    return (a+e+i+o+u)

a = countPerm(3)
print(a)
