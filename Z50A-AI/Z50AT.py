import torch
import numpy
class RL_FC(torch.nn.Module):
    def __init__(self,WOL:list=[5,20,20,1]):
        super().__init__()
        self.L=[]
        i=len(WOL)
        while i>1:
            self.L.append(torch.nn.Linear(WOL[i-2],WOL[i-1]))
            i=i-1
        self.elu=torch.nn.ELU()
        self.L=self.L[::-1]
    def forward(self,x):
        for i in self.L:
            x=i(x)
            x=self.elu(x)
def GetData_FC(jzz:str):
    global ans,que
    jzz2=list(jzz.replace(' ',''))
    for i in range(len(jzz2)):
        jzz2[i]=ord(jzz2[i])
    if len(jzz2)<5:
        jzz2=jzz2+[0,0,0,0,0]
    i2=0
    for i in range(len(jzz2)-4):
        i3=0
        que.append(jzz2[i])
        if jzz2[i]!=0:
            while jzz[i2]==' ':
                i2=i2+1
                i3=i3+1
        que.append(jzz2[i+1])
        if jzz2[i+1]!=0:
            while jzz[i2]==' ':
                i2=i2+1
                i3=i3+1
        que.append(jzz2[i+2])
        if jzz2[i+2]!=0:
            while jzz[i2]==' ':
                i2=i2+1
                i3=i3+1
        que.append(jzz2[i+3])
        if jzz2[i+3]!=0:
            while jzz[i2]==' ':
                i2=i2+1
                i3=i3+1
        que.append(jzz2[i+4])
        if jzz2[i+4]!=0:
            while jzz[i2]==' ':
                i2=i2+1
                i3=i3+1
        ans.append(i3/5)
    que=torch.from_numpy(numpy.array(que)).to(device=dev,dtype=torch.int32).reshape(-1,5)
    ans=torch.from_numpy(numpy.array(ans)).to(device=dev,dtype=torch.int32).reshape(-1,1)
def TrainSet(module=RL_FC,device:str="cuda"):
    global net,op,loss,dev,loss
    dev=device
    net=module().to(device=device)
    op=torch.optim.Adam(net.parameters(),lr=1e-3)
    loss=torch.nn.MSELoss()
def Train(ep:int=1000):
    global ans,que
    for e in range(1,ep+1):
        net.train()
        l=loss(ans,net(que))
        op.zero_grad()
        l.backward()
        op.setp()  