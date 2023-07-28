try:
    from pathlib import Path
    p=list(Path(".").glob("*"))
    a=[str(x) for x in Path(".").iterdir()if x.is_dir()]
    i=0
    while i!=len(a):
        try:
            a=a+[str(x) for x in Path(a[i]).iterdir()if x.is_dir()]
            p=p+list(Path(a[i]).glob("*"))
            i=i+1
        except PermissionError:
            print("文件"+a[i]+"权限不够")
            del a[i]
    del a,i
    d=0
    for i in range(len(p)):
        try:
            with open(str(p[i]),"r")as a:
                a=a.read()
            with open(str(p[i]),"w")as b:
                b.write(a)
            d=d+1
        except OSError:
            pass
        except PermissionError:
            print("文件"+p[i]+"权限不够")
        except UnicodeDecodeError:
            print("文件"+str(p[i])+"编码错误")
        finally:
            pass
    print("处理了"+str(d)+"个文件")
except PermissionError:
    print("权限不够!")
