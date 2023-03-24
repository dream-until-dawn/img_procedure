# pfp类NFT图片合成-支持2-20个图层

## 开发环境
> python 3.9.12

### 所需python库
> Pillow  9.1.0   其安装指令
```shell
    pip install Pillow==9.1.0
```
        

## 使用方法
1. 确保已安装python和Pillow库
2. 在coverage_n图层文件夹下放置pfp类NFT的各个部件。
> 其中1为最底层,20为最高层。
> 文件夹不放置图片脚本就会略过。
> 文件夹原有图片为测试用，放心删除。
> 图片格式只试过.png格式，其它有透明通道的图片格式未试过。
3. 在项目文件下运行 ```shell python start.py ```即可。
4. 输出的图片文件保存在 save 文件夹。
