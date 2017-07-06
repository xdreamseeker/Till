# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    #recursive
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        self.mid_order(root,res)
        for i in range(0,len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True


    def pre_order(self,root):
        if root is None:
            return
        print(root.val,end=",")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def mid_order(self,root,res):
        if root is None:
            return
        self.mid_order(root.left,res)
        res.append(root.val)
        # print(root.val)
        self.mid_order(root.right,res)

    def post_order(self,root):
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val,end=",")

    #non-recursive
    def pre_order_n(self,root):
        stack = []
        leaf = root
        while stack or leaf is not None:
            while leaf is not None:
                print(leaf.val,end=",")
                stack.append(leaf)
                leaf=leaf.left
            if stack:
                leaf =stack.pop()
                leaf = leaf.right

    def mid_order_n(self,root):
        stack = []
        leaf = root
        while stack or leaf is not None:
            while leaf is not None:
                stack.append(leaf)
                leaf=leaf.left
            if stack:
                leaf =stack.pop()
                print(leaf.val,end=",")
                leaf = leaf.right
    #要保证根结点在左孩子和右孩子访问之后才能访问，因此对于任一结点P，先将其入栈。如果P不存在左孩子和右孩子，则可以直接访问它；或者P存在左孩子或者右孩子，但是其左孩子和右孩子都已被访问过了，则同样可以直接访问该结点。若非上述两种情况，则将P的右孩子和左孩子依次入栈，这样就保证了每次取栈顶元素的时候，左孩子在右孩子前面被访问，左孩子和右孩子都在根结点前面被访问。
    def post_order_n(self,root):
        stack = []
        stack.append(root)
        pre = None
        leaf = root
        while stack:
            leaf = stack[-1]
            if (leaf.left is None and leaf.right is None) or (pre is not None and(pre == leaf.left or pre == leaf.right)):
                print(leaf.val,end=",")
                stack.pop()
                pre = leaf
            else:
                if leaf.right is not None:
                    stack.append(leaf.right)
                if leaf.left is not None:
                    stack.append(leaf.left)

    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            leaf = TreeNode(nums[0])
            return leaf

        length = len(nums)
        mid = int(length/2)
        leaf = TreeNode(nums[mid])
        leaf.left = self.sortedArrayToBST(nums[:mid])
        leaf.right = self.sortedArrayToBST(nums[mid+1:])
        return  leaf




#     5
#  3       8
#1  4    6   11
#
if __name__=="__main__":

    app= Solution()
    root = TreeNode(5)
    root.left=TreeNode(3)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(4)

    root.right=TreeNode(8)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(11)
    print(app.isValidBST(root))

    newtree = app.sortedArrayToBST([1,2,3,4,5,6,7,8,9])
    print(app.isValidBST(newtree))
