def extgcd(a, b):
    if b==0:
        return a, 1, 0
    else:
        g, u, v = extgcd(b, a%b)
        q=a//b
        return g, v, u-q*v
def modinverse(a, n):
    g, u, v=extgcd(a, n)
    return u%n
def inzahlen(m):
    result = ''.join(c for c in m if c.isalpha())
    slist = [ord(char) for char in result]

    for n, i in enumerate(slist):
        if i == 97:
            slist[n] = 1
        if i == 98:
            slist[n] = 2
        if i == 99:
            slist[n] = 3
        if i == 100:
            slist[n] = 4
        if i == 101:
            slist[n] = 5
        if i == 102:
            slist[n] = 6
        if i == 103:
            slist[n] = 7
        if i == 104:
            slist[n] = 8
        if i == 105:
            slist[n] = 9
        if i == 106:
            slist[n] = 10
        if i == 107:
            slist[n] = 11
        if i == 108:
            slist[n] = 12
        if i == 109:
            slist[n] = 13
        if i == 110:
            slist[n] = 14
        if i == 111:
            slist[n] = 15
        if i == 112:
            slist[n] = 16
        if i == 113:
            slist[n] = 17
        if i == 114:
            slist[n] = 18
        if i == 115:
            slist[n] = 19
        if i == 116:
            slist[n] = 20
        if i == 117:
            slist[n] = 21
        if i == 118:
            slist[n] = 22
        if i == 119:
            slist[n] = 23
        if i == 120:
            slist[n] = 24
        if i == 121:
            slist[n] = 25
        if i == 122:
            slist[n] = 26
        if i == 228:
            slist[n] = 27
        if i == 246:
            slist[n] = 28
        if i == 252:
            slist[n] = 29
        if i == 223:
            slist[n] = 30

    return slist
def rest_div31(m):

    return m%31
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]
#
#
#
# EINGABEN:
u = input("Nachricht: ")
k = input("Schlüssel: ")
# Nachricht verschlüsseln? 1 Entschlüsseln: 0
Verschlüsseln = input("Nachricht Ver-(1)oder Entschlüsseln?(0): ")
Verschlüsseln= int(Verschlüsseln)
if Verschlüsseln != 1 and Verschlüsseln != 0:
    print("Bitte gültigen Wert für Verschlüsseln (1/0) angeben")
    input("Press Enter to exit")
    exit()
#
#
#
#
Message = inzahlen(u)
AnzahlMessage = len(Message)
#print("Messagezeichen:" , AnzahlMessage)
print("Nachricht in Zahlen:" , Message)

#print("Key:", k)
Key = inzahlen(k)
AnzahlKey = len(Key)
#print("Keyzeichen:", AnzahlKey)
print("Key in Zahlen:" , Key)
KeyLang = []

while len(KeyLang) < len(Message):
    KeyLang.extend(Key)
    if len(KeyLang) > len(Message):
        break
    else:
        if len(KeyLang) == len(Message):
            break

#print("Key auf Messagelänge:", KeyLang, "Länge: ",len(KeyLang))
Zusätzlich = 0
MessageLang = Message
while len(MessageLang) < len(KeyLang):
    MessageLang.extend([1])
    Zusätzlich = Zusätzlich + 1
#print(Zusätzlich)
#print("Message als Vielfaches von Key",MessageLang, "Länge: ", len(MessageLang))


#Inverse des Keys
invers = [modinverse(char, 31) for char in KeyLang]
#print("Key invers: ", invers)


if Verschlüsseln == 1:
    mlist= [KeyLang[i] * MessageLang[i] for i in range(len(MessageLang))]
if Verschlüsseln == 0:
    mlist = [invers[i] * MessageLang[i] for i in range(len(MessageLang))]

#print("Multiplikation",mlist)

Rest = [rest_div31(mlist[x]) for x in range(len(mlist))]

Alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]
res = ""
Ergebnis = [list(Alphabet[Rest[i]]) for i in range(len(Rest))]
Ergebnis = Ergebnis[:len(Ergebnis)-Zusätzlich]
print("Ergebnis als Zahl:",Rest)
res = "".join(str(Ergebnis))
result = ''.join(c for c in res if c.isalpha())
print("Ergebnis: ",result)
input("press Enter to exit")
