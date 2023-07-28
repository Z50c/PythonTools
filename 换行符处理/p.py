from pathlib import Path
p=list(Path(".").glob("*"))
a=[str(x) for x in Path(".").iterdir()if x.is_dir()]
i=0
while i!=len(a):
    a=a+[str(x) for x in Path(a[i]).iterdir()if x.is_dir()]
    p=p+list(Path(a[i]).glob("*"))
    i=i+1
del a
for i in range(len(p)):
    try:
        with open(str(p[i]),"r")as a:
            a=a.read()
        with open(str(p[i]),"w")as b:
            b.write(a)
    except OSError:
        pass
