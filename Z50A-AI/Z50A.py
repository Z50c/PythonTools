Mem=[]#I符号+果+概率*可信度
Bd=3#创新性
from random import randint
while True:
    Out=[]
    In=input("Usr->_: ")+"\n"
    for i in range(len(In)):
        for i2 in range(len(In))[i+1:]:
            a=False
            for i3 in range(len(Mem)):
                if Mem[i3][0]==In[i] and Mem[i3][1]==In[i2]:
                    a=True
                    break
            if a:
                Mem[i3][2]=Mem[i3][2]+1/(i2-i)
            else:
                Mem.append([In[i],In[i2],1/(i2-i)])
    i=len(Mem)-1
    while i!=-1:
        if Mem[i][2]<0.00000000000000000000000000000000000000000000000000000000000000000001:
            del Mem[i]
        else:
            Mem[i][2]=Mem[i][2]/2
            i=i-1
    U=[]
    while True:
        Next=[]
        for i in range(len(In)):
            for i2 in range(len(Mem)):
                if Mem[i2][0]==In[i]:
                    a=False
                    for i3 in range(len(Next)):
                        if Next[i3][0]==Mem[i2][1]:
                            a=True
                            break
                    if a:
                        Next[i3][1]=Next[i3][1]+abs(len(Out)-i)
                    else:
                        Next.append([Mem[i2][1],abs(len(Out)-i)])
        if Bd>len(In):
            i2=len(In)
        else:
            i2=Bd
        N=[]
        while i2!=0:
            ma=0
            for i in Next:
                if i[1]>ma:
                    ma=i[1]
            for i in range(len(Next)):
                if Next[i][1]==ma:
                    N.append(Next[i])
                    break
            del Next[i]
            i2=i2-1
        del Next,i,i2,ma,i3
        a=N[randint(0,len(N)-1)]
        U.append(a)
        a=a[0]
        if a=="\n":
            print(''.join(Out))
            break
        else:
            Out.append(a)
            In=''.join(list(In)+list(a))
        del a
    del U,Out,In
        
                            
