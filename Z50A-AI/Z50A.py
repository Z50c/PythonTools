class ZBot:
    def __init__(self):
        self.Mem=[[],[]]#事件:因+果+概率,因+[设备+果]+概率
        #1.GetQue(触发)
        #2.GetThink(触发)
        #3.WriteThink
        #4.WriteQue
        #5.Asnwer
        self.Think=""
        self.Asn=""
    def Load(self,File:str):
        with open(File,"rb") as File:
            File=File.read()
        #
    def Save(self,File:str):
        #
        with open(File,"wb") as File:
            File.Write()
    def Train(self):
        from random import randint
        Used=[]
        Question=input("In_QueStr:>_ ")
        #Question->Encode->Thinking->Decode->self.Think
        for i in Question:
            P=[]
            for i2 in range(len(self.Mem[0])):
                if self.Mem[0][i2][0]==i:
                    a=False
                    for i3 in P:
                        if self.Mem[0][i2][1]==i3[0]:
                            a=True
                            break
                    if a:
                        P[i3][1]=P[i3][1]+self.Mem[0][i2][2]
                    else:
                        P.append(self.Mem[0][i2][1],self.Mem[0][i2][2])
                    Used.append(i2)
            Max=[0,""]
            for i4 in P:
                if i[0]>Max[0]:
                    Max=i4
            self.Think=self.Think+Max[1]
        print(self.Think)
        Ma=input("Back(-1,0,1): ")
        if Ma=="1":
            for i in Used:
                if self.Mem[0][i][1] in self.Think:
                    self.Mem[0][i][2]=self.Mem[0][i][2]+1
        elif Ma=="-1":
            for i in Used:
                if self.Mem[0][i][1] in self.Think:
                    self.Mem[0][i][2]=self.Mem[0][i][2]-1
        i=0
        del Ma
        Used=[]
        while i!=len(self.Think):
            P=[]
            for i2 in range(len(self.Mem[1])):
                if self.Mem[0][i2][0]==i:
                    a=False
                    for i3 in P:
                        if self.Mem[0][i2][1]==i3[0]:
                            a=True
                            break
                    if a:
                        P[i3][1]=P[i3][1]+self.Mem[1][i2][2]
                    else:
                        P.append(self.Mem[1][i2][1],self.Mem[1][i2][2])
                    Used.append(i2)
            Max=[0,[]]
            for i4 in P:
                if i[0]>Max[0]:
                    Max=i4
            if Max[1][0]==0:
                self.Think=self.Think+Max[1][1]
            elif Max[1][0]==1:
                self.Asn=self.Asn+Max[1][1]
            else:
                print(self.Asn)
                self.Asn=""
                return
        return  
    def Asnwer(self,Question:str):
        pass
    def Guesst(self,Event:str):
        a=input("模式(0-问题->想法,1-想法->其他): ")
        inp=input('输入: ')
        oup=input("输出: ")
        if a=="0":
            Mem=self.Mem[0]
        else:
            Mem=self.Mem[1]
        