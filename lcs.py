def lcs1():
    s1=input("Enter s1: ")
    s2=input("Enter s2: ")
    n,m=len(s1),len(s2)
    
    def help(s1,s2,n,m):
        
        if n==0 or m==0:
            return 0
        if s1[n-1] ==s2[m-1]:
            return 1+help(s1,s2,n-1,m-1)
        else:
            return max(help(s1,s2,n-1,m),help(s1,s2,n,m-1))
    print(help(s1,s2,n,m))

    
def lcs2():
    s1=input("Enter s1: ")
    s2=input("Enter s2: ")
    n,m=len(s1),len(s2)
    arr=[[-1 for _ in range(m+1)]]*(n+1)
    print("i am")
    
    def help(s1,s2,n,m):
        if(n==0 or m==0):
            return 0
        if(arr[n][m]!=-1):
            return arr[n-1][m-1]
        if(s1[n-1]==s2[m-1]):
            arr[n][m]=1+help(s1,s2,n-1,m-1)
        else:
            arr[n][m]=max(help(s1,s2,n-1,m),help(s1,s2,n,m-1))
        return arr[n][m]
    print(help(s1,s2,n,m))
    print(arr)


def lcs3():
    s1=input("Enter s1: ")
    s2=input("Enter s2: ")
    n,m=len(s1),len(s2)
    arr=[[0 for _ in range(m+1)]]*(n+1)
    
    

    for i in range(1,n+1):
        for j in range(1,m+1):
             if(s1[i-1]==s2[j-1]):
                 arr[i][j]=1+arr[i-1][j-1]
             else:
                 arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    print("Enter :",arr[n][m])
    print(arr)
    
    l=[]
    
    while(m>0 and n>0):

        if(s1[n-1]==s2[m-1]):
            l.append(s1[n-1])
            n,m=n-1,m-1
        elif(arr[n-1][m]>=arr[n][m-1]):
            n=n-1
        else:
            m=m-1
        
    print(l)


    

def lcs4():
    s1=input("Enter s1: ")
    s2=input("Enter s2: ")
    n,m=len(s1),len(s2)

    if(n>m):
        n,m=m,n
        s1,s2=s2,s1
    
    arr1=[0]*(n+1)
    arr2=[0]*(n+1)

    for i in range(1,m+1):
        for j in range(1,n+1):
             if(s2[i-1]==s1[j-1]):
                 arr1[j]=1+arr2[j-1]
             else:
                 arr1[j]=max(arr1[j-1],arr2[j])
        arr1,arr2= [0]*(n+1),arr1
    print(arr2[n])

    print(arr2)
    

    

lcs4()
    





