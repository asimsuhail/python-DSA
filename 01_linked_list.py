# sinlge link list implementation in python

class node:
    __data   = None
    __nxtptr = None
    def __init__(self):
        self.__data    = None
        self.__nxtptr  = None

    def setval(self, val):
        self.__data = val
    
    def setnxt(self, nxt):
        self.__nxtptr = nxt

    def getnxt(self):
        return self.__nxtptr
    
    def getval(self):
        return self.__data
    

def insert_at_start(h, val):
    temp = node()
    temp.setnxt(None)
    temp.setval(val)
    if h == None:
        h = temp
    else:
        temp.setnxt(h)
        h = temp
    return h

def display(h):
    cur = node
    cur = h
    while cur != None:
        print(cur.getval())
        cur = cur.getnxt()

head = None

for _ in range(5):
    head = insert_at_start(head, 5)

display(head)
