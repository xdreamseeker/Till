class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Merge(object):
    def merge(self, l1, l2):
        #head.next is the root link
        #to avoid destroy the origin list,so create a new list
        head = Node(0)
        point = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                point.next = Node(l2.val)
                l2 = l2.next
                point = point.next
            elif l2 is None:
                point.next = Node(l1.val)
                l1 = l1.next
                point = point.next
            elif l1.val < l2.val:
                point.next = Node(l1.val)
                l1 = l1.next
                point = point.next
            else:
                point.next = Node(l2.val)
                l2 = l2.next
                point = point.next
        return head.next

    def printList(self,l1):
        while l1 is not None:
            print("%s->"%l1.val,end="")
            l1 = l1.next
        print("END")

if __name__=="__main__":
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next=Node(4)

    l2 = Node(3)
    l2.next = Node(4)
    l2.next.next = Node(4)
    l2.next.next.next = Node(5)
    l2.next.next.next.next = Node(6)

    app = Merge()
    app.printList(l1)
    app.printList(l2)
    newlist = app.merge(l1,l2)
    app.printList(newlist)



