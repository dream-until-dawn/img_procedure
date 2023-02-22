from cgitb import text
import os
import sys
import tkinter as tk

flie_path=os.path.realpath(__file__)
dir_name_list=os.listdir(flie_path+'/../../save/')

window_1 = tk.Tk()
window_1.title('111')
window_1.geometry("400x200")
textE = tk.Text(window_1,height=10)
textE.pack()

def find(f_name):
    flie_name_path = flie_path+"\\..\\..\\save\\"+f_name
    #flie_name_path = "C:\\Users\\10712\\Desktop\\编程文档资料\\project001 - 副本"
    #print(flie_name_path)
    if not f_name in dir_name_list:
        print('文件不存在!')
    os.system('explorer {},/select'.format(flie_name_path))

def getTextInput():
    result=textE.get("1.0","end")    #获取⽂本输⼊框的内容
    print(result.rstrip()+'.png')                          #输出结果
    find(result.rstrip()+'.png')
btnRead=tk.Button(window_1, height=1, width=10, text="查找", command=getTextInput)   #command绑定获取⽂本框内容的⽅法

background = '1景 (4)'#背景
clothing = '1衣 (1)'#衣服
hair = '1头 (1)'#头发
ornament = '1脖饰 (1)'#脖饰
Face_mask = '1空'#口罩
glasses = '3空'#眼镜
flie_name = background+clothing+hair+ornament+Face_mask+glasses+'.png'

btnRead.pack()
window_1.mainloop()



if not len(sys.argv) <= 1:
    #print('带参数！')
    #print(len(sys.argv))
    flie_name =''
    for i in range(1,len(sys.argv)):
        if '(' in sys.argv[i]:
            flie_name+=(' '+sys.argv[i])
        else:
            flie_name+=sys.argv[i]

#flie_name = '1景 (4)1衣 (1)1头 (1)1脖饰 (1)1空3空.png'
#             1景 (4)1衣 (1)1头 (1)1脖饰 (1)1空1镜 (2)
#print(flie_name)
#find(flie_name)