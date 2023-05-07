# sinlge link list implementation in python
class node:
    __data   = None
    __nxtptr = None
    def __init__(self, val, nxt):
        self.__data    = val
        self.__nxtptr = nxt

    def setval(self, val):
        self.__data = val
    
    def setnxt(self, nxt):
        self.__nxtptr = nxt

    def getnxt(self):
        return self.__nxtptr
    
    def getval(self):
        return self.__data
    

def insert_at_start():
    pass


head = node()

for _ in range(5):
    insert_at_start(head)
insert_at_start(head, 7)
