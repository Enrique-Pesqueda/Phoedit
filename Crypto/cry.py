import pickle
from PIL import Image

#a = input("<file:> ")
im = Image.open(input("<Image:> "))
img = im.convert('RGB')

w = img.width
h = img.height

img2 = Image.new('RGB', (w, h), 'white')
ir = Image.new('RGB', (w, h), 'white')

lre = []
lrd = []

lle = []
lld = []

def encrypt():
    print("The Longer it is the better it works!")
    l = input("<Write to crypt:> ")
    key = int(input("<Times to crypt:> "))
    crypt = list(l)
    size = len(crypt)
    #values
    isize = h*w
    k = 0
    print("Loading...")
    for m in range(key):
        for i in range (w):
            k = k%size
            for j in range(h):
                pr,pg,pb = img.getpixel((i,j))
                if m == 0:
                    lre.append(pr)
                pr = (pr + ord(crypt[k]))%256
                pg = (pg + ord(crypt[k]))%256
                pb = (pb + ord(crypt[k]))%256
                k = (k+1)%size
                img2.putpixel((i,j), (pr,pg,pb))
                letter = (ord(crypt[k]) + 1) % 256
                crypt[k] = chr(letter)
    for m in range(key):
        for j in range (w):
            k = k%size
            for i in range(h):
                pr,pg,pb = img2.getpixel((j,i))
                pr = (pr + ord(crypt[k]))%256
                pg = (pg + ord(crypt[k]))%256
                pb = (pb + ord(crypt[k]))%256
                k = (k+1)%size
                img2.putpixel((j,i), (pr,pg,pb))
                letter = (ord(crypt[k]) + 1) % 256
                crypt[k] = chr(letter)
    img2.save("crypto.png")

def decrypt():
    l = input("<key to decrypt:> ")
    key = int(input("<Times to crypt:> "))
    crypt = list(l)
    size = len(crypt)
    #values
    isize = h*w
    k = 0
    print("Loading...")
    for m in range(key):
        for i in range (w):
            k = k%size
            for j in range(h):
                pr,pg,pb = img2.getpixel((i,j))
                #print("pixel: " + str(pr) + " - ord: " + str(ord(crypt[k])))
                pr = (pr - ord(crypt[k]))
                if pr < 0:
                    pr = 256 + pr
                pg = (pg - ord(crypt[k]))
                if pg < 0:
                    pg = 256 + pg
                pb = (pb - ord(crypt[k]))
                if pb < 0:
                    pb = 256 + pb
                k = (k+1)%size
                ir.putpixel((i,j), (pr,pg,pb))
                letter = (ord(crypt[k]) + 1) % 256
                crypt[k] = chr(letter)
    for m in range(key):
        for j in range (w):
            k = k%size
            for i in range(h):
                pr,pg,pb = ir.getpixel((j,i))
                #print("pixel: " + str(pr) + " - ord: " + str(ord(crypt[k])))
                pr = (pr - ord(crypt[k]))
                if pr < 0:
                    pr = 256 + pr
                if m == key-1:
                    lrd.append(pr)
                pg = (pg - ord(crypt[k]))
                if pg < 0:
                    pg = 256 + pg
                pb = (pb - ord(crypt[k]))
                if pb < 0:
                    pb = 256 + pb
                k = (k+1)%size
                ir.putpixel((j,i), (pr,pg,pb))
                letter = (ord(crypt[k]) + 1) % 256
                crypt[k] = chr(letter)
    ir.save("decrypt.png")
    same = 0
    print("lre: " + str(len(lre)))
    print("lrd: " + str(len(lrd)))
    for i in range(len(lre)):
        if lre[i] == lrd[i]:
            #print(str(lre[i]).rjust(3) + " : " + str(lrd[i]).rjust(3) + " Check")
            same+=1
        else:
            print(str(lre[i]).rjust(3) + " : " + str(lrd[i]).rjust(3) + " Wrong")
            pass
    print(str(same) + " / " + str(w*h))

encrypt()
decrypt()
