from tkinter import *
from PIL import Image,ImageTk
import os
import re
'''
background #背景
clothing #衣服
hair #头发
ornament #脖饰
Face_mask #口罩
glasses #眼镜
'''
flie_path=os.path.realpath(__file__)

dir_name_list=os.listdir(flie_path+'/../../save/')
dir_num=len(dir_name_list)
weight_1=[1,2,3,3,3,3,3,4,4]#背景
weight_2=[1]#身体
weight_3=[1,1,1]#衣服
weight_4=[1,1,1,2,2,2]#头发
weight_5=[1,2,2,2]#脖饰
weight_6=[1,1,1,1]#口罩
weight_7=[1,2,3,3,3,3,3]#眼镜
analyse_list=[[0,0,0,0],[0],[0,0],[0,0],[0],[0,0,0]]#出现次数
analyse_list_p_theory=[[0.0384,0.0769,0.5769,0.3076],[0.3333],[0.3333,0.6667],[0.1428,0.8571],[0.25],[0.0555,0.1111,0.8333]]#理论概率

#print(dir_name_list)
for i in range(0,dir_num):
    str_t=dir_name_list[i]
    analyse=list(filter(str.isdigit,re.sub(u"\\(.*?\\)",'',str_t)))
    #print(analyse)
    #print(type(analyse_list[0][int(analyse[0])]))
    #exit()
    analyse_list[0][int(analyse[0])-1]+=1#背景
    analyse_list[1][int(analyse[1])-1]+=1#衣服
    analyse_list[2][int(analyse[2])-1]+=1#头发
    analyse_list[3][int(analyse[3])-1]+=1#脖饰
    analyse_list[4][int(analyse[4])-1]+=1#口罩
    analyse_list[5][int(analyse[5])-1]+=1#眼镜
#背景 衣服 头发 脖饰 口罩 眼镜
#print(analyse_list)

#--------------------------------------------------------------------------------------------------------------------------------------------
radio_win = Tk()
radio_win.title('nft查找')
radio_win.geometry('1280x720')


l = Label(radio_win, bg='yellow', width=35, text='empty')
l.grid(row=8,column=10)
l_2 = Label(radio_win, bg='yellow', width=15, text='empty')
l_2.grid(row=10,column=10,sticky=W)
l_3 = Label(radio_win, bg='yellow', width=15, text='empty')
l_3.grid(row=10,column=10,sticky=E)

def ply(x,y):
    return analyse_list_p_theory[x][int(y[0])-1]

def ply_r(x,y):
    return analyse_list[x][int(y[0])-1]/10000

def print_selection():
    l.config(text='')
    l.config(text=v.get()[:-4]+c.get()[:-4]+h.get()[:-4]+o.get()[:-4]+f.get()[:-4]+g.get()[:-4])

def find():
    f_name = v.get()[:-4]+c.get()[:-4]+h.get()[:-4]+o.get()[:-4]+f.get()[:-4]+g.get()[:-4]+'.png'
    flie_name_path = flie_path+"\\..\\..\\save\\"+f_name
    #flie_name_path = "C:\\Users\\10712\\Desktop\\编程文档资料\\project001 - 副本"
    #print(flie_name_path)
    l_2.config(text='')
    l_2.config(text='理论概率:{:.2f}%'.format(ply(0,v.get())*ply(2,h.get())*ply(3,o.get())*ply(5,g.get())*100))
    if not f_name in dir_name_list:
        l_3.config(text='')
        l_3.config(text='文件不存在')
    else:
        l_3.config(text='')
        l_3.config(text='实际概率:{:.2f}%'.format(ply_r(0,v.get())*ply_r(2,h.get())*ply_r(3,o.get())*ply_r(5,g.get())*100))
        os.system('explorer {},/select'.format(flie_name_path))


Button(radio_win,text='查找',command=find).grid(row=9,column=10)

v = StringVar()
v.set('1景 (4).png')
c = StringVar()
c.set('1衣 (1).png')
h = StringVar()
h.set('1头 (1).png')
o = StringVar()
o.set('1脖饰 (1).png')
f = StringVar()
f.set('1空.png')
g = StringVar()
g.set('1镜 (2).png')
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_7\\1景 (4).png')
img_1 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\2景 (2).png')
img_2 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\3景 (1).png')
img_3 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\3景 (5).png')
img_4 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\3景 (6).png')
img_5 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\3景 (8).png')
img_6 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\3景 (9).png')
img_7 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\4景 (3).png')
img_8 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_7\\1景 (4).png')
img_9 = ImageTk.PhotoImage(img.resize((60, 60)))

Label(radio_win,width=8, text='背景').grid(row=7,column=0)
Radiobutton(radio_win,variable=v,value='1景 (4).png',image=img_1,command=print_selection,activebackground='blue').grid(row=7,column=1)
Radiobutton(radio_win,variable=v,value='2景 (2).png',image=img_2,command=print_selection,activebackground='blue').grid(row=7,column=2)
Radiobutton(radio_win,variable=v,value='3景 (1).png',image=img_3,command=print_selection,activebackground='blue').grid(row=7,column=3)
Radiobutton(radio_win,variable=v,value='3景 (5).png',image=img_4,command=print_selection,activebackground='blue').grid(row=7,column=4)
Radiobutton(radio_win,variable=v,value='3景 (6).png',image=img_5,command=print_selection,activebackground='blue').grid(row=7,column=5)
Radiobutton(radio_win,variable=v,value='3景 (8).png',image=img_6,command=print_selection,activebackground='blue').grid(row=7,column=6)
Radiobutton(radio_win,variable=v,value='3景 (9).png',image=img_7,command=print_selection,activebackground='blue').grid(row=7,column=7)
Radiobutton(radio_win,variable=v,value='4景 (3).png',image=img_8,command=print_selection,activebackground='blue').grid(row=7,column=8)
Radiobutton(radio_win,variable=v,value='4景 (7).png',image=img_9,command=print_selection,activebackground='blue').grid(row=7,column=9)
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_5\\1衣 (1).png')
img_h = img.size[0]
img_w = img.size[1]
x = img_w * 0.3
y = img_h * 0.7
crop_w = img_w *0.3
crop_h = img_h * 0.3
clothing_1 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_5\\1衣 (2).png')
clothing_2 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_5\\1衣 (3).png')
clothing_3 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))

Label(radio_win,width=8, text='衣服').grid(row=6,column=0)
Radiobutton(radio_win,variable=c,value='1衣 (1).png',image=clothing_1,command=print_selection,activebackground='blue').grid(row=6,column=1)
Radiobutton(radio_win,variable=c,value='1衣 (2).png',image=clothing_2,command=print_selection,activebackground='blue').grid(row=6,column=2)
Radiobutton(radio_win,variable=c,value='1衣 (3).png',image=clothing_3,command=print_selection,activebackground='blue').grid(row=6,column=3)
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_4\\1头 (1).png')
hair_1 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_4\\1头 (3).png')
hair_2 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_4\\1头 (4).png')
hair_3 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_4\\2头 (2).png')
hair_4 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_4\\2头 (5).png')
hair_5 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_4\\2头 (6).png')
hair_6 = ImageTk.PhotoImage(img.resize((60, 60)))

Label(radio_win,width=8, text='头发').grid(row=5,column=0)
Radiobutton(radio_win,variable=h,value='1头 (1).png',image=hair_1,command=print_selection,activebackground='blue').grid(row=5,column=1)
Radiobutton(radio_win,variable=h,value='1头 (3).png',image=hair_2,command=print_selection,activebackground='blue').grid(row=5,column=2)
Radiobutton(radio_win,variable=h,value='1头 (4).png',image=hair_3,command=print_selection,activebackground='blue').grid(row=5,column=3)
Radiobutton(radio_win,variable=h,value='2头 (2).png',image=hair_4,command=print_selection,activebackground='blue').grid(row=5,column=4)
Radiobutton(radio_win,variable=h,value='2头 (5).png',image=hair_5,command=print_selection,activebackground='blue').grid(row=5,column=5)
Radiobutton(radio_win,variable=h,value='2头 (6).png',image=hair_6,command=print_selection,activebackground='blue').grid(row=5,column=6)
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_3\\1脖饰 (1).png')
img_h = img.size[0]
img_w = img.size[1]
x = img_w * 0.4
y = img_h * 0.6
crop_w = img_w *0.2
crop_h = img_h * 0.2
ornament_1 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_3\\2脖饰 (2).png')
ornament_2 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_3\\2脖饰 (3).png')
ornament_3 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_3\\2空.png')
ornament_4 = ImageTk.PhotoImage(img.crop((x,y,x+crop_w,y+crop_h)).resize((60, 60)))

Label(radio_win,width=8, text='脖饰').grid(row=4,column=0)
Radiobutton(radio_win,variable=o,value='1脖饰 (1).png',image=ornament_1,command=print_selection,activebackground='blue').grid(row=4,column=1)
Radiobutton(radio_win,variable=o,value='2脖饰 (2).png',image=ornament_2,command=print_selection,activebackground='blue').grid(row=4,column=2)
Radiobutton(radio_win,variable=o,value='2脖饰 (3).png',image=ornament_3,command=print_selection,activebackground='blue').grid(row=4,column=3)
Radiobutton(radio_win,variable=o,value='2空.png',image=ornament_4,command=print_selection,activebackground='blue').grid(row=4,column=4)
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_2\\1空.png')
Face_mask_1 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_2\\1口罩 (1).png')
Face_mask_2 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_2\\1口罩 (2).png')
Face_mask_3 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_2\\1口罩 (3).png')
Face_mask_4 = ImageTk.PhotoImage(img.resize((60, 60)))

Label(radio_win,width=8, text='口罩').grid(row=3,column=0)
Radiobutton(radio_win,variable=f,value='1空.png',image=Face_mask_1,command=print_selection,activebackground='blue').grid(row=3,column=1)
Radiobutton(radio_win,variable=f,value='1口罩 (1).png',image=Face_mask_2,command=print_selection,activebackground='blue').grid(row=3,column=2)
Radiobutton(radio_win,variable=f,value='1口罩 (2).png',image=Face_mask_3,command=print_selection,activebackground='blue').grid(row=3,column=3)
Radiobutton(radio_win,variable=f,value='1口罩 (3).png',image=Face_mask_4,command=print_selection,activebackground='blue').grid(row=3,column=4)
#-----------------------------------------------------------------------------------
img=Image.open(flie_path+'\\..\\..\\coverage_1\\1镜 (2).png')
glasses_1 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\2镜 (1).png')
glasses_2 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\3镜 (3).png')
glasses_3 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\3镜 (4).png')
glasses_4 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\3镜 (5).png')
glasses_5 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\3镜 (6).png')
glasses_6 = ImageTk.PhotoImage(img.resize((60, 60)))
img=Image.open(flie_path+'\\..\\..\\coverage_1\\3空.png')
glasses_7 = ImageTk.PhotoImage(img.resize((60, 60)))

Label(radio_win,width=8, text='眼镜').grid(row=2,column=0)
Radiobutton(radio_win,variable=g,value='1镜 (2).png',image=glasses_1,command=print_selection,activebackground='blue').grid(row=2,column=1)
Radiobutton(radio_win,variable=g,value='2镜 (1).png',image=glasses_2,command=print_selection,activebackground='blue').grid(row=2,column=2)
Radiobutton(radio_win,variable=g,value='3镜 (3).png',image=glasses_3,command=print_selection,activebackground='blue').grid(row=2,column=3)
Radiobutton(radio_win,variable=g,value='3镜 (4).png',image=glasses_4,command=print_selection,activebackground='blue').grid(row=2,column=4)
Radiobutton(radio_win,variable=g,value='3镜 (5).png',image=glasses_5,command=print_selection,activebackground='blue').grid(row=2,column=5)
Radiobutton(radio_win,variable=g,value='3镜 (6).png',image=glasses_6,command=print_selection,activebackground='blue').grid(row=2,column=6)
Radiobutton(radio_win,variable=g,value='3空.png',image=glasses_7,command=print_selection,activebackground='blue').grid(row=2,column=7)
#-----------------------------------------------------------------------------------



radio_win.mainloop()