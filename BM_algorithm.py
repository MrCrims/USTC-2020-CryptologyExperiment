import copy
#用键来表示指数，对应值就是系数
def Ploy_plus(TD,BD,m):
    CD = {}
    temp = {}
    for key in BD.keys():#乘上D^m就是把每一个键直接加m
        temp[key+m] = BD[key]
    keys = list(TD.keys()) + list(temp.keys())

    keys = list(set(keys))
    for i in keys:
        if i in TD or i in temp:
            CD[i] = 1
        if i in TD and i in temp:
            CD[i] = 0
    for i in keys:
        if CD[i] == 0:
            del CD[i]
    return CD

def BM(bits):
    TD = {}
    CD = {0:1}
    BD = {0:1}
    L = [0]
    l = 0
    m = 0
    d = 0
    for i in range(0,len(bits)):
        j = 0
        d = 0
        temp = bits[i-l:i+1]
        temp.reverse()
        for s in temp:#求Dn
            if j not in CD:
                d += 0
            else:
                d += CD[j]*int(s)
            j += 1
        d = d%2
        m += 1
        if d == 0:
            L.append(l)
        else:
            TD = copy.deepcopy(CD)
            CD = Ploy_plus(CD,BD,m)
            if l < i/2 :
                l = i+1-l
                L.append(l)
                BD = copy.deepcopy(TD)
                m = 0
        if l >= 10000:
            return "The LSFR is too big!"
    return [CD,L]

if __name__ == '__main__':
    txt_name = "Ex2_Ciph.txt"
    temp = ''
    with open(txt_name,'r') as f:
        for i in f:
            for j in i[:2500]:
                temp += bin(ord(j))

    bits = temp.replace("0b","")
    bits = list(bits)
    LFSR = BM(bits)
    if type(LFSR) == 'str':
        print(LFSR)
    else:
        L = max(LFSR[1])
        fn = ''
        CD = LFSR[0]
        for key in CD.keys():
            if key == 0:
                fn += '1'
            else:
                fn += '+x^' + str(key)
        print("连接多项式为:", fn, "级数为", L)
        