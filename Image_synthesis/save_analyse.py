import os
import re

flie_path=os.path.realpath(__file__)

dir_name_list=os.listdir(flie_path+'/../../save/')
dir_num=len(dir_name_list)
analyse_list=[[0,0,0,0],[0],[0,0],[0,0],[0],[0,0,0]]
#print(dir_name_list)
#背景 衣服 头发 脖饰 口罩 眼镜

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


print('共统计{0}条\n背景权重一出现{1}次\t二出现{2}次\t三出现{3}次\t四出现{4}次\n头发权重一出现{5}次\t二出现{6}次\n眼镜权重一出现{7}次\t二出现{8}次\t三出现{9}次\n脖饰权重一出现{10}次\t二出现{11}次'
.format(dir_num,analyse_list[0][0],analyse_list[0][1],analyse_list[0][2],analyse_list[0][3],analyse_list[2][0],analyse_list[2][1],analyse_list[5][0],analyse_list[5][1],analyse_list[5][2],analyse_list[3][0],analyse_list[3][1]))
print('稀有率:')
print('背景权重一:{}%\t背景权重二:{}%\t背景权重三:{}%\t背景权重四:{}%'
.format(analyse_list[0][0]/10000*100,analyse_list[0][1]/100,analyse_list[0][2]/100,analyse_list[0][3]/100))
print('头发权重一:{}%\t头发权重二:{}%'
.format(analyse_list[2][0]/10000*100,analyse_list[2][1]/100))
print('眼镜权重一:{}%\t眼镜权重二:{}%\t眼镜权重三:{}%'
.format(analyse_list[5][0]/10000*100,analyse_list[5][1]/100,analyse_list[5][2]/100))
print('头发权重一:{}%\t头发权重二:{}%'
.format(analyse_list[3][0]/10000*100,analyse_list[3][1]/100))
#print(analyse_list)

exit()
flie_name = dir_name_list[0]
flie_name_path = flie_path+"\\..\\..\\save\\"+flie_name
#flie_name_path = "C:\\Users\\10712\\Desktop\\编程文档资料\\project001 - 副本"
print(flie_name_path)
os.system('explorer {},/select'.format(flie_name_path))

