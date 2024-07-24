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
    return strencode
#Thomas's Code
def decode(password):
    intpass = list(password)
    threestring = ""
    listofnumbers = list(password)
    for nums in range(len(listofnumbers)):
        addnum = int(listofnumbers[nums]) - 3
        if addnum < 0:
            addnum += 10
        threestring += str(addnum)
    return threestring
