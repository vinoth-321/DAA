import heapq
from collections import Counter,defaultdict 

class Node:
    def __init__(self,char=None,fre=0):
        self.char=char
        self.fre=fre
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.fre < other.fre
    
    
def huffman(word):
    frequency=Counter(word)
    heap=[Node(char,fre) for char,fre in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        newnode=Node(None,left.fre+right.fre)
        heapq.heappush(heap,newnode)
        newnode.left=left
        newnode.right=right
    root=heap[0]

    code={}
    def codeis(root,cur=""):
        if( root is None):
           return 
        if  root.char is not None:
           
            code[root.char]=cur
        codeis(root.left,cur+"0")
        codeis(root.right,cur+"1")

    codeis(root)
    return code,frequency

def encode(code,str):
    return "".join(code[char] for char in str)


def decode(code,huffcode):
    rev={c:char for char,c in huffcode.items()}
    cur,ans="",""

    for i in code:
        cur+=i
        if cur in rev:
            ans+=rev[cur]
            cur=""
    return ans


huffcode,frequency=huffman("hello huffman")
print(huffcode)
code=encode(huffcode,"hello huffman")
str=decode(code,huffcode)
print(code)
print(str)

        