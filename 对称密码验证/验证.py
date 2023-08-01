class Key:
    def __init__(self,Key:str,Time:int=16,Limit:int=65536):
        def a(b,c):
            return b-b//c*c
        self.__Limit=Limit
        self.Time=Time
        self.__Key=[a(ord(Key[i]),self.__Limit) for i in range(len(Key))]
        self.__Tick=0
    def Gen(self,x:int):
        k=self.__Key.copy()
        t=self.Time
        def a(b,c):
            return b-b//c*c
        while t!=0:
            for i in range(len(k)):
                i2=0
                for i3 in k:
                    i2=i2+i3
                k[i]=a(i2,self.__Limit)
            t=t-1
        del i,i2,i3
        d=0
        for i in range(len(k)):
            d=a(d+(x**i)*k[i],self.__Limit)
        return d
    def Verify(self,x:int,y:int):
        d=self.Gen(x)
        print(d)
        if self.__Tick==len(self.__Key):
            self.__Tick=0
            self.Time=self.Time-1
            if self.Time==-1:
                self.Time=0
        if d==y:
            return True
        else:
            return False