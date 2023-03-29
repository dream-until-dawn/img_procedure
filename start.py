from PIL import Image
import os

flie_path = os.path.realpath(__file__)


def get_filename(n):
    file_name_list = os.listdir(flie_path+'/../coverage_'+str(n))
    file_name = str(file_name_list)
    file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
    file_name = file_name.split(',')
    return file_name


ImgName = {}  # 所有图片名字
for x in range(0, 20):
    keyName = "coverage_"+str(20-x)
    result = get_filename(20-x)
    if ((len(result) >= 1) & (result[0] != "")):  # 大于0长度在加入
        ImgName[keyName] = result
print("查找图片完成:")
for key, value in ImgName.items():
    print("文件夹{}下{}张图片,图片文件名:\t{}".format( key, len(value), " ".join(x for x in value)))


max_count = 1
for x in ImgName.values():
    max_count *= len(x)
input("可合成出{}张,按下任意键确认,退出同时按下  Ctrl+C".format(max_count))


ImgObjest = []  # 所有需拼接的透明通道
for key, value in ImgName.items():  # 拿到键值对
    ImgObjest_z = []
    for img in value:  # 遍历拿到文件名
        ImgObjest_z.append(Image.open((flie_path+'/../{0}/{1}').format(key, img)))  # 得到所有需拼接的透明通道
    ImgObjest.append(ImgObjest_z)

compoundList_max = [len(x) for x in ImgObjest]
max_compoundList = len(compoundList_max)


def recursion(base_img,img_x,img_str):#传进的底图，二维数组x位置，所经途径,计数
    if(img_x >= (max_compoundList-1)):#只剩最后一段了,就保存图片准备退出
        for img_y in range(0,compoundList_max[img_x]):#取得他在x位置的y 遍历
            base_img_copy = base_img.copy()#复制
            r,g,b,a = ImgObjest[img_x][img_y].split()
            base_img_copy.paste(ImgObjest[img_x][img_y],(0,0),a)#叠加
            saveFileName = img_str+str(img_y)
            base_img_copy.save(flie_path+'/../save/{0}.png'.format(saveFileName))
            print("合成{}.png成功".format(saveFileName))
        return
    else:
        for img_y in range(0,compoundList_max[img_x]):#取得他在x位置的y 遍历
            base_img_copy = base_img.copy()#复制
            r,g,b,a = ImgObjest[img_x][img_y].split()
            base_img_copy.paste(ImgObjest[img_x][img_y],(0,0),a)#叠加
            recursion(base_img_copy,img_x+1,img_str+str(img_y))#后面还有就继续递归


for y in range(0,compoundList_max[0]):#第一层有几个可能值
    baseImg = ImgObjest[0][y]  # 拿到第一层做底
    recursion(baseImg,1,str(y))
        


