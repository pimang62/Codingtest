class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # shell에 출력되는 method!
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount

    def popAt(self, pos):
        # 삭제할때는 nodeCount 보다 큰 index가 없기 때문에 "+1" 을 제외
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        prev = self.getAt(pos-1)
        curr = self.getAt(pos)
        
        # 유일한 노드일 때
        if self.nodeCount == 1:
            self.head = None
            self.tail = None

        else:
            # 맨 앞 원소를 뽑고 싶을 때
            if pos == 1:
                self.head = curr.next
            
            # 뽑는 값이 마지막 값일 때
            elif curr.next == None:
                self.tail = prev
                prev.next = None
            
            # 중간값일 때
            else:
                prev.next = curr.next
            
        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

'''
>>> from linkedlist import *
>>> a = Node(67)
>>> b = Node(34)
>>> c = Node(46)
>>> L = LinkedList()
>>> L
LinkedList: empty
>>> L.insertAt(1, a)
True
>>> L
67
>>> L.insertAt(2, b)
True
>>> L
67 -> 34
>>> L.insertAt(2, c)
True
>>> L
67 -> 46 -> 34
'''