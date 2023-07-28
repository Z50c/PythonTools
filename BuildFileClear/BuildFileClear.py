from pathlib import Path
import os
p=list(Path(".").glob("*.o"))
a=[str(x) for x in Path(".").iterdir()if x.is_dir()]
i=0
while i!=len(a):
    a=a+[str(x) for x in Path(a[i]).iterdir()if x.is_dir()]
    p=p+list(Path(a[i]).glob("*.o"))
    i=i+1
del a
for i in p:
    if os.path.isfile(i):
        os.remove(i)

