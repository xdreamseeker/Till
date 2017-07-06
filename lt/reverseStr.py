class Solution():
    def reverseStr(self,str):
        length = len(str)
        if length < 2:
            return str

        str = list(str)
        for i in range(0,int(length/2)):
            str[i],str[length-1-i]=str[length-1-i],str[i]

        str="".join(str)
        return str

if __name__=="__main__":
    app = Solution()
    str = "e"

    print(app.reverseStr(str))