ans=[]
def get(n):
    for i in range(n):
        yield i 

def isvalid(state):
    m=len(state)-1
    for i in range(m):
        if state[i]==state[m] or abs(state[i]-state[m])==abs(i-m):
            return False
    return True


def backtrack(state,n):
    if len(state)==n:
        ans.append(state.copy())
        return
    
    for canditate in get(n):
        state.append(canditate)
        if isvalid(state):
            backtrack(state,n)
        state.pop()
state=[]
backtrack(state,4)
print(ans)
