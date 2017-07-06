# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA = 0
        lengthB = 0

        papre=None
        pbpre=None
        pa = headA
        pb = headB

        while pa:      #while pa
            lengthA += 1
            papre = pa
            pa = pa.next

        while pb:
            lengthB += 1
            papre = pb
            pb = pb.next

        if papre != papre:
            return None

        if lengthA > lengthB:
            diff = lengthA-lengthB
            pa = headA
            pb = headB
            for i in range(0,diff):
                pa=pa.next
            for i in range(0,lengthB):
                if pa == pb:
                    return pa
                else:
                    pa = pa.next
                    pb = pb.next

        elif lengthA < lengthB:
            diff = lengthB-lengthA
            pa = headA
            pb = headB
            for i in range(0,diff):
                pb=pb.next
            for i in range(0,lengthA):
                if pa == pb:
                    return pa
                else:
                    pa = pa.next
                    pb = pb.next
        else:
            pa = headA
            pb = headB
            for i in range(0,lengthA):
                if pa == pb:
                    return pa
                else:
                    pa = pa.next
                    pb = pb.next



if __name__=="__main__":
    app = Solution()

