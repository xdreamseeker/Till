class Solution(object):
    #(A)x(B)，它的下一个排列是：(A)y(B’)，其中A、B和B’是“字符串”(可能为空），x和y是“字符”，前缀相同，都是A，且一定有y > x。
    #21543  23145
    def nextString(self, str):
        if len(str) < 2:
            return
        index = self.__findTail(str)
        if index == 0:
            return "EOF"
        head = str[0:index-1]
        # x = str[index-1]
        tail = str[index:]
        newtail = tail[::-1]  #字符串反转
        index2 = self.__findY(newtail,str[index-1])
        newtail = list(newtail)
        y = newtail[index2]
        newtail[index2] = str[index-1]
        newtail = "".join(newtail)
        newstr = head+y+newtail
        return newstr

    def __findTail(self,str):
        for index in range(len(str) -1,-1,-1):
            if str[index] > str[index-1]:
                return index
        return index

    def __findY(self,newtail,numx):
        for i in range(0,len(newtail)):
            if newtail[i] >numx:
                return i
        return i


if __name__=="__main__":
    app = Solution()
    str = "123"
    res = app.nextString(str)
    while res != "EOF":
        print(res)
        res = app.nextString(res)