class Solution(object):
    # c[i] = int((a[i]) xor int(b[i])  tmp=int((a[i]) and int(b[i])
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()

        lengthA = len(a)
        lengthB = len(b)


        if lengthB>lengthA:
            a,b = b,a
            lengthA,lengthB = lengthB,lengthA

        c=[0]*(lengthA+1)
        for i in range(lengthB,lengthA):
            b.append(0)

        tmp = 0
        for i in range(0,lengthA):
            c[i] = int(a[i]) ^ int(b[i]) ^ tmp
            tmp = (int(a[i]) & int(b[i]))|(int(a[i]) & tmp)|((int(b[i]) & tmp))
        c[lengthA] =tmp
        if c[lengthA] == 0:
            c = c[:lengthA]
        c.reverse()
        res =[]
        for value in c:
            res.append(str(value))
        res="".join(res)
        return res




if __name__=="__main__":
    app = Solution()

    print(app.addBinary("1000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111","1"))