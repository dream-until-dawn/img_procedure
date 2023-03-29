from PIL import Image, ImageSequence
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

ImgObjest = []  # 所有需拼接的git帧列表[[[1,2,3,4,5,...]],[],[]]
for key, value in ImgName.items():  # 拿到键值对
    ImgObjest_z = []
    for img in value:  # 遍历拿到文件名
        frame_list = [] # 帧列表
        image_x = Image.open((flie_path+'/../{0}/{1}').format(key, img))  # 打开图片
        for frame_1 in ImageSequence.Iterator(image_x):
            frame_list.append(frame_1.convert('RGBA'))
        ImgObjest_z.append(frame_list)  # 得到所有需拼接的帧列表
    ImgObjest.append(ImgObjest_z)

compoundList_max = [len(x) for x in ImgObjest]
max_compoundList = len(compoundList_max)


def recursion(base_img,frame_count,img_x,img_str):#传进的底图，当前帧数，二维数组x位置，所经途径,计数
    # print('第{}层第{}张第{}帧,路径:{}'.format(1,img_x,frame_count+1,img_str))
    if(img_x >= (max_compoundList-1)):#只剩最后一段了,就保存图片准备退出
        # print("最后一层递归，准备返回")
        frameList = []
        for img_y in range(0,compoundList_max[img_x]):#取得他在x位置的y 遍历
            base_img_copy = base_img.copy() # 复制
            new_frame_1 = Image.alpha_composite(base_img_copy, ImgObjest[img_x][img_y][frame_count]) # 叠加上
            saveFileName = img_str+str(img_y)
            # print("返回:{}，路径:{}".format(new_frame_1,saveFileName))
            frameList.append([new_frame_1,saveFileName])
        return frameList
    else:
        return_list = []
        for img_y in range(0,compoundList_max[img_x]):#取得他在x位置的y 遍历
            # print("递归，路径:{}".format(img_str+str(img_y)))
            base_img_copy = base_img.copy() # 复制
            new_frame_1 = Image.alpha_composite(base_img_copy, ImgObjest[img_x][img_y][frame_count]) # 叠加上
            result = recursion(new_frame_1,frame_count,img_x+1,img_str+str(img_y)) # 后面还有就继续递归
            return_list.extend(result)
        return return_list


frame_dict = {}
print('第一层有{}可能,列表:{}'.format(compoundList_max[0],compoundList_max))
for y in range(0,compoundList_max[0]):#第一层有几个可能值
    print('第一层第{}张有{}帧数'.format(y+1,len(ImgObjest[0][0])))
    save_list = {}
    for z in range(0,len(ImgObjest[0][0])): # 遍历帧次数
        # print('开始递归第{}层第{}张第{}帧'.format(1,y+1,z+1))
        baseImg = ImgObjest[0][y][z]  # 拿到第一层第z帧做底
        result = recursion(baseImg,z,1,str(y))
        for row in result:
            if(row[1] in frame_dict.keys()):
                frame_dict[row[1]].append(row[0])
            else:
                frame_dict[row[1]] = []
                frame_dict[row[1]].append(row[0])
        print('第{}帧执行完毕'.format(z+1))

max_count = len(frame_dict.keys())
count = 0
print("开始合成!")
for key,value in frame_dict.items():
    count += 1
    value[0].save('./save/{}#{}.gif'.format(key,count),
               save_all=True,  # 保存所有帧
               append_images=value[1:],
               duration=100,
               loop=0)
    print("进度({})/({})".format(count,max_count))