x=0
f=open('PARY_LICZB.TXT').read()
y=f.split("\n")
for i in y:
    try:
        l1 = i.split()
        try:
            if int(l1[0]) % int(l1[1]) == 0:
                x+=1
            elif int(l1[1]) % int(l1[0]) == 0:
                x+=1
        except IndexError:
            pass
    except ValueError:
        pass
print(x)