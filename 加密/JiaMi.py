try:
    f=input("要加密/解密的文件:")
    with open(f,'rb') as a:
        a=a.read()
        print(a)
    with open(input("密码本:"),'rb') as b:
        b=b.read()
        print(a)
    i=len(a)
    i2=len(b)
    c=b''
    while i!=0:
        i=i-1
        i2=i2-1
        if i2==-1:
            i2=len(b)-1
        c=c.__add__((a[i]^b[i2]^b[i2]).to_bytes())
    print(c)
    if len(f)>=6:
        if f[-6:]==".MWPyH":
            with open(f[:-6],"wb") as a:
                a.write(c)
        else:
            with open(f+".MWPyH","wb") as a:
                a.write(c)
    else:
        with open(f+".MWPyH","wb") as a:
            a.write(c)
except FileNotFoundError:
    print('文件找不到')
except PermissionError:
    print('权限不足')
