a=open("slowa.txt").read()
p=open("hasla.txt","w")
z=open("wyniki.txt","w")
l=a.split("\n")
for slowo in l:
    print(slowo[::-1])
maks=0
mins=len(l[0])
for slowo in l:
    if len(slowo)>maks:
        maks=len(slowo)
        maxs=slowo
    if len(slowo)<mins:
        mins=len(slowo)
        minss=slowo
print(minss, mins, maxs, maks)
p.close()