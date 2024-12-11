import sys
sys.setrecursionlimit(2147483647)

class Linked:
    def __init__(self):
        self.data = None
        self.next = None
    
    def read(self):
        data = []
        if self.data != None:
            data.append(self.data)
        if self.next != None:
            data += self.next.read()
        return data
    
    def count(self):
        if self.data == None:
            return 0
        return 1 + self.next.count()

def buildlist(data):
    linkedlist = Linked()
    next = linkedlist

    for i in range(len(data)):
        next.data = data[i]
        next.next = Linked()
        next = next.next
    
    return linkedlist

def blink(stones : Linked):
    if stones == None or stones.data == None:
        return

    length = len(str(stones.data))
    if length % 2 == 0:
        copy = stones.data
        stones.data = int(str(copy)[:length // 2])

        next = stones.next
        stones.next = Linked()
        stones.next.data = int(str(copy)[length // 2:])
        stones.next.next = next
    else:
        next = stones.next

        if stones.data == 0: 
            stones.data = 1 
        else: 
            stones.data *= 2024
            
    blink(next)

data = [int(x) for x in open("input.txt").readline().split(" ")]
stones = buildlist(data)
print(stones.read())

for _ in range(25):
    blink(stones)

print(stones.count())