from itertools import count
from PIL import Image
import os

flie_path=os.path.realpath(__file__)

def get_filename(n):
    file_name_list = os.listdir(flie_path+'/../../coverage_'+str(n))
    file_name = str(file_name_list)
    file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
    file_name = file_name.split(',')
    return file_name
list_1=get_filename(5)
list_2=get_filename(4)
list_3=get_filename(3)
list_4=get_filename(2)
list_5=get_filename(1)

count_num=1
max_num=len(list_1)*len(list_2)*len(list_3)*len(list_4)*len(list_5)
print('预计合成 {0} 张图片，请等待...'.format(max_num))

#quit()
for i_1 in list_1:
    im_1=Image.open((flie_path+'/../../coverage_5/{0}').format(i_1))
    image_1=im_1.copy()#打开第1张

    for i_2 in list_2:
        im_2=Image.open((flie_path+'/../../coverage_4/{0}').format(i_2))
        image_2=im_2.copy()#打开第2张

        for i_3 in list_3:
            im_3=Image.open((flie_path+'/../../coverage_3/{0}').format(i_3))
            image_3=im_3.copy()#打开第3张

            for i_4 in list_4:
                im_4=Image.open((flie_path+'/../../coverage_2/{0}').format(i_4))
                image_4=im_4.copy()#打开第4张

                for i_5 in list_5:
                    im_5=Image.open((flie_path+'/../../coverage_1/{0}').format(i_5))
                    image_5=im_5.copy()#打开第5张
                    #--------------------------------------------------------------------
                    r,g,b,a = image_2.split()
                    image_1.paste(image_2,(0,0),a)#叠加第2张
                    r,g,b,a = image_3.split()
                    image_1.paste(image_3,(0,0),a)#叠加第3张
                    r,g,b,a = image_4.split()
                    image_1.paste(image_4,(0,0),a)#叠加第4张
                    r,g,b,a = image_5.split()
                    image_1.paste(image_5,(0,0),a)#叠加第5张
                    #--------------------------------------------------------------------
                    image_1.save(flie_path+'/../../save/{0}{1}{2}{3}{4}.png'.format(i_5[:-4],i_4[:-4],i_3[:-4],i_2[:-4],i_1[:-4]))
                    print('合成第{0}张,进度---({1}/{2})'.format(count_num,count_num,max_num))
                    count_num+=1


