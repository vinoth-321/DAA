import numpy as np
def get_size(n):
    return 1 if n==0 else (2**(n-1).bit_length())

def padding(a,n):
    pad=np.zeros((n,n),dtype=a.dtype)
    pad[:a.shape[0],:a.shape[1]]=a
    return pad
def update(c,n):
    return c[:n[0],:n[1]]

def matix(a,b):
    assert a.shape[1]==b.shape[0] ,"invalid"

    m,k=a.shape
    _,n=b.shape

    size=get_size(max(m,k,n))

    pad_a=padding(a,size)
    pad_b=padding(b,size)

    c=stressan(a,b)

    return update(c,(m,n))


def stressan(a,b):
    n=a.shape[0]
    if n==1:
        return np.array([[a.item() * b.item()]])

    mid=n//2
    a11=a[:mid,:mid]
    a12=a[:mid,mid:]
    a21=a[mid:,:mid]
    a22=a[mid:,mid:]

    b11=b[:mid,:mid]
    b12=b[:mid,mid:]
    b21=b[mid:,:mid]
    b22=b[mid:,mid:]

    m1=stressan(a11+a22,b11+b22)
    m5=stressan(a11+a12,b22)
    m3=stressan(a11,b12-b22)
    m4=stressan(a22,b21-b11)
    m2=stressan(a21+a22,b11)
    m7=stressan(a12-a22,b21+b22)
    m6=stressan(a21-a11,b11+b12)

    c1=m1+m4-m5+m7
    c2=m3+m5
    c3=m2+m4
    c4=m1-m2+m3+m6

    top=np.hstack((c1,c2))
    bottom=np.hstack((c3,c4))
    ans=np.vstack((top,bottom))

    return ans
    

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
])

B = np.array([
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
])

C = matix(A, B)
print("Strassen Result:\n", C)


