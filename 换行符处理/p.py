from pathlib import Path

p=list(Path(".").glob("*"))

for i in range(len(p)):

    try:

        with open(str(p),"r")as a:

            a=a.read()

        with open(str(p),"w")as b:

            b.write(a)

    except OSError:

        pass
