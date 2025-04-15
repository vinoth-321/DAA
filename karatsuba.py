def karatsuba(s1,s2):
    if len(s1)<4 or len(s2)<4:
        return str(int(s1)*int(s2))
    
    n=max(len(s1),len(s2))
    if n%2 !=0:
        n+=1
    s1=s1.zfill(n)
    s2=s2.zfill(n)

    half=n//2

    h1,l1=s1[:half],s1[half:]
    h2,l2=s2[:half],s2[half:]

    x=karatsuba(l1,l2)
    y=karatsuba(str(int(h1)+int(l1)),str(int(h2)+int(l2)))
    z=karatsuba(h1,h2)

    a=z+"".zfill(half*2)
    b=str(int(y)-int(z)-int(x))+"".zfill(half)

    
    return str(int(a)+int(b)+int(x))


print(karatsuba("100000","1000000"))