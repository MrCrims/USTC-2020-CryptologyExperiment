import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import  matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
#
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
            temp = temp.replace('-', '')
            temp = temp.replace('"', '')
            temp = temp.replace(':', '')
            temp = temp.replace('(', '')
            temp = temp.replace(')', '')
            temp = temp.replace('\'','')
            temp = temp.replace(';', '')
            temp = temp.replace('`', '')
            temp = temp.strip('\n')
    f.close()
    return temp
file_name = input('Please put in the file name:')
passage = read_message(file_name)
#
def count_single_char(passage):#用字典存储每个字母对应的频数
    dic={}
    for i in range(-1,len(passage)):
        if passage[i] in dic:
            dic[passage[i]]+=1
        if passage[i] not in dic:
            dic[passage[i]]=1
    return dic
dic_single = count_single_char(passage)
#
def draw_hitogram(dic):#画直方图
    x_data=[i for i in dic.keys()]
    y_data=[]
    for i in dic.keys():
        y_data.append(dic[i])
    plt.bar(x=x_data,height=y_data,label='Single_char_analyse',color='steelblue',alpha=0.8)
    for x,y in enumerate(y_data):
        plt.text(x,y,'%s'%y,ha='center',va='bottom')
    plt.xlabel('字母')
    plt.ylabel('频数')
    plt.legend()
    plt.show()
draw_hitogram(dic_single)
#
def VigenereCode(passage):#对明文用Vigenre密码加密
    Key=input('Please input your own key:')
    Key.lower()
    l_key=len(Key)
    Code=''
    for i in range(0,len(passage)):
        temp=(ord(passage[i])-97+ord(Key[i%l_key])-97)%26
        Code+=chr(temp+65)
    return Code
Ciphertext=VigenereCode(passage)
#
def write_in_txt(Ciphertext):#将密文写入到txt文档中
    with open('D:\CryExperiments\Ex1_Ciph.txt','w+') as f:
        f.write(Ciphertext)
write_in_txt((Ciphertext))
#
