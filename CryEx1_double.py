import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import  matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar3D
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
#
def read_message(txt_name):#从txt文档中读取明文,将所有明文并在一起，不分段
    temp=''
    with open('D:\CryExperiments\Ex1_Ciph.txt','r') as f:
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
            temp = temp.replace('\'', '')
            temp = temp.replace(';', '')
            temp = temp.replace('`', '')
            temp = temp.strip('\n')
    f.close()
    return temp
file_name = input('Please put in the file name:')
passage = read_message(file_name)
#
def count_double_char(passage):#用字典存储双字符对应的频数
    dic={}
    for i in range(0,26):
        for j in range(0,26):
            key=chr(i+97)+chr(j+97)
            dic[key]=0
            key=''
    for i in range(0,len(passage)-1):
        key=passage[i]+passage[i+1]
        dic[key]+=1
        key=''
    return dic
dic_double=count_double_char(passage)
#
def draw_3Dhitogram(dic_double):#画3D直方图
    x_data=[]
    z_data=[]
    for i in range(0,26):
        x_data.append(chr(i+97))
    y_data=x_data
    for i in dic_double.keys():
        i_x=ord(i[0])-97
        i_y=ord(i[1])-97
        z_data.append([i_x,i_y,dic_double[i]])
    chart=(
        Bar3D().add(
            "",
            z_data,
            xaxis3d_opts=opts.Axis3DOpts(x_data, type_="category", max_=26),
            yaxis3d_opts=opts.Axis3DOpts(y_data, type_="category", max_=26),
            zaxis3d_opts=opts.Axis3DOpts(type_="value", max_=60),
            grid3d_opts=opts.Grid3DOpts(width="280", height="100"))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1),
            title_opts=opts.TitleOpts(title="双字符统计")
        )
        )
    return chart
chart=draw_3Dhitogram(dic_double)
chart.render("double_chart.html")
