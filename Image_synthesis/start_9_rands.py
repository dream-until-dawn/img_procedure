from PIL import Image
import os
import random

flie_path=os.path.realpath(__file__)

def get_filename(n):
    file_name_list = os.listdir(flie_path+'/../../coverage_'+str(n))
    #file_name = str(file_name_list)
    file_name = file_name_list
    #file_name = file_name.replace("[", "").replace("]", "").replace("'", "")#.replace(" ", "")
    #file_name = file_name.split(',')
    return file_name
list_1=get_filename(9)
list_2=get_filename(8)
list_3=get_filename(7)
list_4=get_filename(6)
list_5=get_filename(5)
list_6=get_filename(4)
list_7=get_filename(3)
list_8=get_filename(2)
list_9=get_filename(1)

#print(list_7)
#加权数组
weight_1=[1,1,1]#背景
weight_2=[1,1]#腿
weight_3=[1,1]#后腿
weight_4=[1,1]#身体
weight_5=[1,1,1,1,1]#眼睛
weight_6=[1,1,1,1,1,1,1,1,1]#嘴
weight_7=[1,1]#微章
weight_8=[1,1]#头
weight_9=[1,1]#前手
#print(len(dir_num))
#for i in range(1,100):
    #print(random.choices(list_1,weights=weight_1))
#exit()

count_num=1
max_num=len(list_1)*len(list_2)*len(list_3)*len(list_4)*len(list_5)*len(list_6)*len(list_7)*len(list_8)*len(list_9)
max_list1=len(list_1)
max_list2=len(list_2)
max_list3=len(list_3)
max_list4=len(list_4)
max_list5=len(list_5)
max_list6=len(list_6)
max_list7=len(list_7)
max_list8=len(list_8)
max_list9=len(list_9)
max_t=100
save_name='string'


print('预计合成 {0} 张图片，请等待...'.format(max_t))
for count_t in range(1,max_t*3):
    save_name=''
    dir_num=len(os.listdir(flie_path+'/../../save/'))
    if dir_num >= max_t:
        print('已完成{0}张，共进行{1}次图片合成。'.format(dir_num,count_t))
        break
    #--------------------------------------------------------------------
    random_value=random.choices(list_1,weight_1)[0]#随机取值
    save_name+=random_value[:-4]
    im_1=Image.open((flie_path+'/../../coverage_9/{0}').format(random_value))
    image_1=im_1.copy()#打开第1张

    random_value=random.choices(list_2,weight_2)[0]#随机取值
    #save_name+=random_value[:-4]
    im_2=Image.open((flie_path+'/../../coverage_8/{0}').format(random_value))
    image_2=im_2.copy()#打开第2张

    random_value=random.choices(list_3,weight_3)[0]#随机取值
    save_name+=random_value[:-4]
    im_3=Image.open((flie_path+'/../../coverage_7/{0}').format(random_value))
    image_3=im_3.copy()#打开第3张

    random_value=random.choices(list_4,weight_4)[0]#随机取值
    save_name+=random_value[:-4]
    im_4=Image.open((flie_path+'/../../coverage_6/{0}').format(random_value))
    image_4=im_4.copy()#打开第4张

    random_value=random.choices(list_5,weight_5)[0]#随机取值
    save_name+=random_value[:-4]
    im_5=Image.open((flie_path+'/../../coverage_5/{0}').format(random_value))
    image_5=im_5.copy()#打开第5张

    random_value=random.choices(list_6,weight_6)[0]#随机取值
    save_name+=random_value[:-4]
    im_6=Image.open((flie_path+'/../../coverage_4/{0}').format(random_value))
    image_6=im_6.copy()#打开第6张

    random_value=random.choices(list_7,weight_7)[0]#随机取值
    save_name+=random_value[:-4]
    im_7=Image.open((flie_path+'/../../coverage_3/{0}').format(random_value))
    image_7=im_7.copy()#打开第7张

    random_value=random.choices(list_8,weight_8)[0]#随机取值
    save_name+=random_value[:-4]
    im_8=Image.open((flie_path+'/../../coverage_2/{0}').format(random_value))
    image_8=im_8.copy()#打开第8张

    random_value=random.choices(list_9,weight_9)[0]#随机取值
    save_name+=random_value[:-4]
    im_9=Image.open((flie_path+'/../../coverage_1/{0}').format(random_value))
    image_9=im_9.copy()#打开第9张
    #--------------------------------------------------------------------
    r,g,b,a = image_2.split()
    image_1.paste(image_2,(0,0),a)#叠加第2张
    r,g,b,a = image_3.split()
    image_1.paste(image_3,(0,0),a)#叠加第3张
    r,g,b,a = image_4.split()
    image_1.paste(image_4,(0,0),a)#叠加第4张
    r,g,b,a = image_5.split()
    image_1.paste(image_5,(0,0),a)#叠加第5张
    r,g,b,a = image_6.split()
    image_1.paste(image_6,(0,0),a)#叠加第6张
    r,g,b,a = image_7.split()
    image_1.paste(image_7,(0,0),a)#叠加第7张
    r,g,b,a = image_8.split()
    image_1.paste(image_8,(0,0),a)#叠加第8张
    r,g,b,a = image_9.split()
    image_1.paste(image_9,(0,0),a)#叠加第9张
    #--------------------------------------------------------------------
    image_1.save(flie_path+'/../../save/{0}.png'.format(save_name))
    print('合成第{0}张,已完成进度---({1}/{2}),共有{3}'.format(count_num,dir_num+1,max_t,max_num))
    count_num+=1

