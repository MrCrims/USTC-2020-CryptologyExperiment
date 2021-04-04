def read_message(txt_name):#从txt文档中读取明文,将所有明文并在一起，不分段
    temp=''
    with open(txt_name,'r') as f:
        for i in f:
            temp += i.lower()
            temp = temp.replace(',', '')
            temp = temp.replace(' ', '')
            temp = temp.replace('!', '')
            temp = temp.replace('?', '')
            temp = temp.replace('.', '')
            temp = temp.replace('(', '')
            temp = temp.replace(')', '')
            temp = temp.replace('\'', '')
            temp = temp.replace(';', '')
            temp = temp.replace('`', '')
            temp = temp.replace('-', '')
            temp = temp.replace('"', '')
            temp = temp.replace(':', '')
            temp = temp.strip('\n')
    f.close()
    return temp
file_name = input('Please put in the file name:')
passage = read_message(file_name)
#
def count_triple_char(passage):#统计三字符频率
    dic={}
    for i in range(0,26):
        for j in range(0,26):
            for k in range(0,26):
                key=chr(i+97)+chr(j+97)+chr(k+97)
                dic[key]=0
    for i in range(0,len(passage)-2):
        key=passage[i]+passage[i+1]+passage[i+2]
        dic[key]+=1
    return dic
dic_triple=count_triple_char(passage)
#
def get_label(dic_triple):#获取至少出现四次的三字符的下标
    label = []
    for i in dic_triple.keys():
        if dic_triple[i] > 3:
            label.append(i)
    return label
label = get_label(dic_triple)
#
def get_gap(label):#获取选取出的每个三字符对应的下标集合
    count = 0
    total_gap = []
    for i in label:
        temp = 0
        index_find = 0
        total_gap.append([])
        while temp != -1:
            temp = passage.find(i,index_find,len(passage))
            if temp != -1 :
                total_gap[count].append(temp)
                index_find = len(i)+temp#找到的是结尾的label
        count += 1
    return total_gap
total_gap = get_gap(label)
#
def make_gap(total_gap):#获取每个三字符下标组组内的间隔列表
    temp = []
    count = 0
    for i in total_gap:
        for j in range(0,i.__len__()-1):
            temp.append(i[j+1]-i[j])
        total_gap[count] = temp[:]
        count += 1
        temp.clear()
    return total_gap
total_gap = make_gap(total_gap)
gcd = []
for i in total_gap:#求各个三字符的gcd，并存放在一个列表中
    temp = 1
    for j in range(1,min(i)):
        for k in i:
            if k%j != 0:
                break
        if k == i[i.__len__()-1]:
            temp = j
    gcd.append(temp)
print(label)
print(gcd)
print(label.__len__())
count = 0
for i in gcd:
    if i == 4:
        count += 1
print(count/label.__len__())
count = 0
num = 0
for i in gcd:
    if i%4 == 0:
        count += 1
print(count/label.__len__())