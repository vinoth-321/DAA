import numpy as np
def simple(tab):
    nrow,ncol=tab.shape
    nvar=ncol-nrow


    while True:
        zrow=tab[-1,:-1]
        
        if np.all(zrow >=0):
            break

        pi_col=np.argmin(zrow)
        print("Pivot column:", pi_col)
        print("Pivot column entries in constraints:", tab[:-1, pi_col])
        if np.all(tab[:-1,pi_col]<=0):
            print(tab[:-1,pi_col])
            raise ValueError("Unbounded Solution : yes")
        
        ratio=[]
        for i in range(nrow-1):
            if(tab[i,pi_col]>0):
                ratio.append(tab[i,-1]/tab[i,pi_col])
            else:
                ratio.append(np.inf)
        pi_row=np.argmin(ratio)

        val=tab[pi_row,pi_col]
        tab[pi_row,:]/=val

        for i in range(nrow):
            if i !=pi_row:
                tab[i,:]-=tab[i,pi_col]*tab[pi_row,:]

    for i in range(nvar):
        print("x: ",tab[i,-1])
    print("x: ",tab[-1,-1])  



tableau = np.array([
    [1, 2, 1, 0, 8],
    [3, 2, 0, 1, 12],
    [-3, -5, 0, 0, 0]  # Objective function (negated for max)
], dtype=float)

simple(tableau)

