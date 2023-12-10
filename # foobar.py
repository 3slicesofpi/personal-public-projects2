# foobar
# if 3 foo if 5 bar 15 foobar else nothing

raw = []
def extendlist(targetLen,raw):
    curLen = 0
    while targetLen > 0:
        targetLen -= 1
        curLen += 1
        raw.append(curLen)
    return sorted(raw)

extendlist(16,raw)

def foobar(format,raw):
    for x in raw:
        if (x % 3) == 0:
            mod3Exist = "foo"
        else:
            mod3Exist = ""

        if (x % 5) == 0:
            mod5Exist = "bar"
        else:
            mod5Exist = ""

        if format == 1:
            print(str(x) + " " + mod3Exist + mod5Exist)
        elif format == 0:
            print(mod3Exist + mod5Exist)
        else:
            print("error, input format; 0,1")

foobar(1,raw)
    





