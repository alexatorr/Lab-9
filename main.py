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
if __name__=='__main__':
    option=0
    while option!=3:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option=int(input('Please enter an option: '))
        if option==1:
            password=str(input('Please enter your password to encode: '))
            a=encode(password)
            print('Your password has been encoded and stored!')
            print('')
        elif option==2:
            print(f'The encoded password is {a}, and the original password is {decode(a)}.')
    exit()