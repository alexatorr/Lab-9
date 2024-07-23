def encode(password):
    intpass = list(map(int,password))
    passencode=[]
    i=0
    while i<=len(intpass)-1:
        a=(intpass[i]+3)
        passencode.append(a)
        i=i+1
    strencode=''.join(str(passencode))
    print(strencode)
encode('12345555')