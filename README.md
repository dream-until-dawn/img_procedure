# pfp类NFT图片合成-支持N多图层

## 开发环境
> python 3.9.12

#### 所需python库
> Pillow  9.1.0   其安装指令
```shell
    pip install Pillow==9.1.0
```
        

## 使用方法
1. 确保已安装python和Pillow库
2. 在coverage_n图层文件夹下放置pfp类NFT的各个部件。需要几层自己新建文件夹,文件名为"coverage_"加上数字。
> **其中1为最底层,无穷大为最高层**。

> 文件夹不放置图片脚本就会略过。

> 文件夹原有图片为测试用，放心删除。

> 图片格式只试过.png格式，其它有透明通道的图片格式未试过。

3. 在项目文件下运行 ```python start.py```即可。
4. 输出的图片文件保存在 save 文件夹。


# pfp类gif动态图NFT合成-支持N多图层

## 开发环境
> python 3.9.12

#### 所需python库
> Pillow  9.1.0   其安装指令
```shell
    pip install Pillow==9.1.0
```
        

## 使用方法
1. 确保已安装python和Pillow库
2. 在coverage_n图层文件夹下放置pfp类NFT的各个部件。自己新建文件夹,文件名为"coverage_"加上数字。
> <span style="color:red;">**其中无穷大为最底层,1为最高层**。</span>

> git合成是按帧先合成,再把连续帧合成为成品。所以准备时间较长,等每帧都合成完了才会开始输出图片。

> 文件夹不放置图片脚本就会略过。

> 文件夹原有图片为测试用，放心删除。

> 图片格式只试过.gif格式，其它有透明通道的图片格式未试过。

3. 在项目文件下运行 ```python startGIF.py```即可。
4. 输出的图片文件保存在 save 文件夹。

### 后续完善
> 1. 加入异步以提高合成速度。