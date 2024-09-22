def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])