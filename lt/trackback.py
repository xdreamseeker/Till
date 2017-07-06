class Solution():
    def trackback(self,list):
        res = []
        self.dfs(list,[],res)
        print(res)

    def dfs(self,list,oneres,res):
        if len(list) == 1:
            oneres.append(list[0])
            res.append(oneres)
        else:
            for i in range(0,len(list)):
                self.dfs(self.delindex(list,i),oneres+[list[i]],res)

    def delindex(self,list,index):
        res = []
        res = list[:index]+list[index+1:]
        return res

if __name__=="__main__":
    app = Solution()
    list=list("123")
    res = app.trackback(list)
    print(res)

    # print(app.delindex(list("123"),1))