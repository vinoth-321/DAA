import math
def mat(dim):
    n=len(dim)-1
    arr=[[0 for i in range(n+1)]for i in range(n+1)]
    s=[[0 for i in range(n+1)]for i in range(n+1)]

    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            arr[i][j]=math.inf
            for k in range(i,j):
                cost=arr[i][k]+arr[k+1][j]+(dim[i-1]*dim[k]*dim[j])
                if cost<arr[i][j]:
                    arr[i][j]=cost
                    s[i][j]=k

    return arr[1][n],s

def  point(s,i,j):
    if(i==j):
        return f"A{i}"
    else:
        k=s[i][j]
        left=point(s,i,k)
        right=point(s,k+1,j)
        return f"({left}*{right})"

dim=[40, 20, 30, 10, 30]
cost,s=mat(dim)
print("Cost :",cost)
print("Optimal :",point(s,1,len(dim)-1))