#Alexa's code
def encode(password):
    intpass = list(password)
    passencode=''
    i=0
    while i<=len(intpass)-1:
        a=int(intpass[i])+3
        if a>=10:
            a=a-10
        passencode=passencode+str(a)
        i=i+1
    strencode=''.join(str(passencode))
    print(strencode)
encode('12345555')
encode('00009962')