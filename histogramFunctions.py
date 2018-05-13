#*******************************************************************************************************
# histogramFunctions.py
# Contributors: Tristan Martin
# Last Changed: 14 April 2018
# Description:
#*******************************************************************************************************
import pickle
from PIL import Image

#*******************************************************************************************************
# Summary:
def img2list(w,h,img,l):
    r,g,b = [],[],[]
    add = [0]*3
    for i in range(w):
        for j in range(h):
            r.append(img.getpixel((i,j))[0])
            g.append(img.getpixel((i,j))[1])
            b.append(img.getpixel((i,j))[2])
    l[0],l[1],l[2] = r,g,b
    return l
#*******************************************************************************************************
# Summary:
def write2txt(dico):
    with open('average.txt', 'w') as f:
        f.write(str(dico))
#*******************************************************************************************************
# Summary:
def sortList(l, dico):
    for i in range(len(l)):
        sorted(l[i])
        put2dico(l[i],i, dico)
    return l
#*******************************************************************************************************
# Summary:
def put2dico(l, i, dico):
    for k in range(len(l)):
        if i == 0:
            dico['red'][l[k]] += 1
        elif i == 1:
            dico['green'][l[k]] += 1
        elif i == 2:
            dico['blue'][l[k]] += 1
#*******************************************************************************************************
# Summary:
def avg(l):
    l2 = [0]*3
    for i in range(len(l)):
        for j in range(len(l[i])):
            l2[i] += l[i][j]
        l2[i] = l2[i]/(w*h)
        l2[i] = (l2[i]/256)*100
    return l2
#*******************************************************************************************************
# Summary:
def histr(ir, dico):
    n = 0
    k = parcours('red', dico)
    for elt in dico['red']:
        pcg = (elt / (k))*100
        n+=1
        for i in range (n-1,n):
            for j in range(int(pcg)):
                ir.putpixel((i,j), (180,0,0))
    ir2 = ir.transpose(Image.FLIP_TOP_BOTTOM)
    ir2.save('images/red.png')
#*******************************************************************************************************
# Summary:
def histg(ig, dico):
    n = 0
    k = parcours('green', dico)
    for elt in dico['green']:
        pcg = (elt / (k))*100
        n+=1
        for i in range (n-1,n):
            for j in range(int(pcg)):
                ig.putpixel((i,j), (0,180,0))
    ig2 = ig.transpose(Image.FLIP_TOP_BOTTOM)
    ig2.save('images/green.png')
#*******************************************************************************************************
# Summary:
def histb(ib, dico):
    n = 0
    k = parcours('blue', dico)
    for elt in dico['blue']:
        pcg = (elt / (k))*100
        n+=1
        for i in range (n-1,n):
            for j in range(int(pcg)):
                ib.putpixel((i,j), (0,0,180))
    ib2 = ib.transpose(Image.FLIP_TOP_BOTTOM)
    ib2.save('images/blue.png')
#*******************************************************************************************************
# Summary:
def parcours(color, dico):
    n = 0
    for i in dico[color]:
        if n <= i:
            n = i
    return n
#*******************************************************************************************************
# Summary:
def run(picToUse):
    #Task1
    dico = {
        'red' : [0]*256,
        'green' : [0]*256,
        'blue' : [0]*256
    }

    l = [[]]*3
    a = picToUse
    img = Image.open(a)
    w = img.width
    h = img.height

    ir = Image.new('RGB', (256, 100), 'white')
    ig = Image.new('RGB', (256, 100), 'white')
    ib = Image.new('RGB', (256, 100), 'white')

    finalList = sortList(img2list(w,h,img,l), dico)
    histr(ir, dico)
    histg(ig, dico)
    histb(ib, dico)
