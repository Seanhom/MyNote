#                                           OpenCV轻松入门 ： 面向python



## 第1章 OpenCV入门

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201106163216326.png" alt="image-20201106163216326"  />

#### 1.2.1 读取图像

##### 1.imread() : 读取图像

```python
retval = cv2.imread(filename[, flag])             #flag为可选项  
"""
brief: 读取图像
param1:  filename : 要读取的图像的完整文件名
param2： flag: 读取标记。该标记用来控制读取文件的类型。
return:  retval: 图像数组，未读取到图像，返回“None”。
"""
```

![image-20201109104925492](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109104925492.png)

#### 1.2.2 显示图像

##### 1. namewindow() : 创建指定名称的窗口

```python
cv2.namewindow(winname)
"""
brief: 创建指定名称的窗口
param1:  winname是要创建的窗口的名称。
param2： 
return:  
"""
```

##### 2.imshow() : 显示图像

```python
None = cv2.imshow(winname,mat)
```

- winname: 窗口名称
- mat：要显示的图像

##### 3.waitKey()：等待按键

```python
retval = cv2.waitKey([delay])
```

- retval :  没有按键按下，返回-1 ； 有被按下，则返回按键ASCII值。
- delay ： 等待按键被触发的时间，默认为 0 。

##### 4.destroyWindow() : 释放指定窗口

```python
None = cv2.destroyWindow(winname)
```

##### 5.destoryAllWindiws() : 释放所有窗口。

```python
None = cv2.destroyAllWindow(winname)
```





#### 1.2.3 保存图像

##### 1.imwrite() :  保存图像

```python
retval = cv2.imwrite(filename,img [,params])
```

- retval ： True /False
- filename : 要保存的目标文件的完整路径名。
- img : 被保存图像的名称。
- params: 保存类型参数，可选。



#### 1.2.4 OpenCV库

![image-20201107130904127](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107130904127.png)









## 第2章 图像处理基础

![image-20201107130958109](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107130958109.png)

**知识点把握：**

- 图像 的基本表示方法
- 像素的访问和操作
- 感兴趣区域处理
- 通道处理



### 2.1 图像的基本表示方法

3种基本表示方法：二值图像、灰度图像、彩色图像。

#### 2.1.1 二值图像

- 1. 仅仅包含白色和黑色。
  2. 计算机将白色像素点处理为“1”，黑色像素点处理为“0”

- 1. 每个像素点只有两种取值，因此只使用 1 个bit 就能表示（0 或 1）

#### 2.1.2 灰度图像

- 1. 每个像素点取值 ∈ [0.255]
  2. "0"  代表纯黑色；“255"代表纯白色；其余的数值表示从纯白到纯黑之间不同级别的灰度。
- 1.  每个像素点用 1 个 Byte表示（8bit）
  2. 灰度图来表示二值图，像素点只有数值0和数组255两种类型的取值。

#### 2.1.3 彩色图像

- 1. 人的视网膜上有3种不同的颜色感受器。
  2. 从光学角度、心理学角度等出发，会有不同的表述颜色的模式。
  3. 我们常用的是RGB色彩空间。
- 1. 计算机通常用3维数组表示RGB彩色图像。
  2. 图像通道的顺序是 R $\rightarrow$ G  $\rightarrow$ B
  3. OpenCV的通道顺序为  B $\rightarrow$ G  $\rightarrow$ R
  4.  每个色彩通道，像素值∈[0.255]
- 可以根据需要对不同色彩空间的图像进行类型转换。灰$\rightarrow$ 二，彩$\rightarrow$ 灰。



### 2.2 像素处理

可以通过**位置索引**的形式对图像内的元素进行访问、处理。

 **二值图及灰度图像** ：Numpy库中的二维数组。二值图理解为特殊的灰度图。

**彩色图像：** 三维ndarray。

### 2.3 使用numpy.array访问像素

numpy.array 提供了 **item()**  和 **itemset() ** 来访问和修改像素值。

使用numpy.array提供的函数比直接使用索引要快得多。

#### 2.3.1 二值图像及灰度图像

##### 1.item() : 访问图像像素点

```python
item(行，列)
```

##### 2.itemset() : 修改像素值

```python
itemset(索引值，新值)
```

#### 2.3.2 彩色图像

##### 1.item() : 访问图像像素点

```python
item(行，列，通道)
```

##### 2.setitem() :修改像素值

```python
setitem(三元组索引值，通道)
```





### 2.4 感兴趣区域（ROI）

可能会对图像的某一特定区域感兴趣，可以对该区域进行整体操作，例如赋值。

![image-20201107153520364](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107153520364.png)

### 2.5 通道操作

##### 1.通道拆分： cv2.split()

- 索引拆分![image-20201107153843166](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107153843166.png)
- 函数的方式![image-20201107153945169](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107153945169.png)

##### 2.通道合并：cv2.merge()

```python
b,g,r=cv2.split(lena)
bgr=cv2.merge([b,g,r])
```



### 2.6 获取图像属性

##### 1.shape：返回图像的类型

- 返回值：
  1. 彩色：三维
  2. 灰度或二值：二维

##### 2.size ： 图像的像素数目，其值为 “行x列x通道数” 。

##### 3.dtype ：返回图像的数据类型。





## 第3章 图像的运算

![image-20201107154951909](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107154951909.png)

​                                                 ​![image-20201107155002637](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107155002637.png)  

**知识点把握：**

- 图像的加法运算、位运算
- 利用加法、位运算实现：位平面分解、图像异或加密、数字水印、脸部打码/解码等实例。



### 3.1 加法运算

可以通过加号运算符，也可以通过 cv2.add()

##### 1.加号运算符

![image-20201107172924848](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107172924848.png)

像素值超过255，对256取余数。

##### 2.cv2.add()： 计算图像像素值相加的和

![image-20201107173214824](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201107173214824.png)

像素值若大于255，则取255.

```python
retval = cv2.add(参数A，参数B)
```

- 参数A，B均可以为数值、图像

### 3.2 图像加权和



图像加权和定义：计算两幅图像的像素之和时，将每副图像的权重考虑进来。公式表示为：![image-20201108092635500](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108092635500.png)

##### 3.2.1 cv2.addWeighted()

```python
dst = cv2.addWeighted(src1,apha,src2,beta,gamma)
```

可以理解为： **结果图像 = 图像1x系数1 +  图像2x系数2 + 亮度调节量**



### 3.3 按位逻辑运算

所谓的位逻辑运算，即将数值转换为**二进制**后，在对应的位置上进行**位运算**。 

##### 1.cv2.bitwise_and() : 按位与

```python
dst = cv2.bitwise_and(src1 , src2 [,mask])
```

- dst : 与输入值具有同样大小的array输出值。
- src1 : 第一个array或scalar类型的输入值。
- src2 : 第二个array或scalar类型的输入值。
- mask：可选操作掩码，8位单通道array

##### 2.cv2.bitwise_not() : 按位或

##### 3.cv2.bitwise_xor() :  按位异或

##### 4.cv2.bitwise_not() : 按位非

一般操作为，构造一个掩模图像（src2），使用某种位运算保留图像中被掩模指定的部分。

### 3.4 掩模mask

OpenCV中，许多函数都会指定一个掩模，也称为掩码。例如：

```python
计算结果 = cv2.add(参数1，参数2，掩模)
```

当使用掩模运算时，操作只会在掩模值为非空的像素点上中执行，并将其他像素点的值置为0 。

mask是8位单通道array，无法直接与彩色图像完成掩模运算。可以将mask转换成BGR模式的彩色图像，从而完成与彩色图像的掩模运算。

### 3.5 图像与数值的运算

在上述的加法运算和按位运算中，参与运算的两个算子既可以是两幅图像，也可以是一副图像和一个数值。

例如：想增加图像的整体亮度，可以将每一个像素值都加上一个固定值。



### 3.6 位平面分解

在8位的灰度图中，每一个像素使用8位二进制来表示，即灰度值取值范围在[0,255]，可以将每个像素值表示为：

![image-20201108105438726](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108105438726.png)

通过提取灰度图像素点   **二进制像素值**   的每一  **比特位**  的组合，可以得到多个**位平面图像**。

在8位灰度图中，可以组成8个二进制值图像，即可以将原图分解为8个位平面。

**原图O：**

![image-20201108112149595](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108112149595.png)

**其对应的二进制值为：**

![image-20201108112228683](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108112228683.png)

**8个位平面：**

![image-20201108112301746](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108112301746.png)







**位平面分解的具体步骤：**以灰度图像为例

​                                            **1.图像预处理**   ：   读取图像O，获得图像宽M和高N。

​                                                        $\Downarrow$

​                                             **2. 构造提取矩阵** 

​                                                       $\Downarrow$ 

​				              		   	**3. 提取位平面**

​                                                       $\Downarrow$

​                                             **4.阈值处理**

​                                                       $\Downarrow$

​                                             **5.显示图像**



### 3.7 图像加密和解码

通过按位异或运算可以实现图像的加密和解密

![image-20201108113859565](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108113859565.png)

- a :  明文，原始数据
- b：密钥 。 
- c ：密文，通过xor(a,b)来实现。

![image-20201108114206691](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108114206691.png)



### 3.8 数字水印

**最低有效位（LSB）：**  指的是一个二进制图像中的第0位。

**最低有效位信息隐藏：** 将载体图像的最低有效位层替换为当前需要隐藏的二值图像，从而实现将二值图隐藏的目的。

隐藏后的二值图无法通过肉眼观察出含水印载体图像和原始图像的不同，水印的隐蔽性较高。

这种信息隐藏技术也称为数字水印，通过该方式可以实现信息隐藏、版权认证、身份认证等功能。

数字水印信息可以是文本、视频、音频等多种形式。这里仅讨论数字水印是二值图的情况。

原始图像、水印图像均可以为彩色图像，这时需要对它们进行通道分解、图层分解，后续处理方法与二值水印图像的处理方法相同。

**水印嵌入过程流程图：**

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108145233516.png" alt="image-20201108145233516"  />



**水印提取过程流程图：**

![image-20201108145330794](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108145330794.png)



### 3.9 脸部打码及解码

使用    **掩模 **  和    **按位运算**    方式实现的对脸部打码、解码。





## 第4章  色彩空间类型转换 

![image-20201108152121131](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108152121131.png)



**知识点把握：**

**常见的色彩空间：** GRAY（灰度）、XYZ、YCrCb、HSV、HLS等等

每个色彩空间都有自己擅长的处理问题的领域，为了更方便地处理某个具体问题，就要用到色彩空间类型的转换。



### 4.1 色彩空间基础

#### 4.1.1 Gray

GRAY通常指8位灰度图，具有256个灰度级，像素值的范围是[0,255]

**RGB $\longrightarrow$  GRAY**  :

```python
# opencv常用转换方式
Gray = 0.299·R + 0.587·G + 0.114·B

#简化形式
Gray = (R+G+B)/3
```



**GRAY $\longrightarrow$  RGB** :

```python
R = GRAY
G = GRAY
B = GRAY
```



#### 4.1.2 YCrCb

人眼视觉系统对  **颜色**  的敏感度要低于对  **亮度**  的敏感度。

YCrCb空间中，Y 代表**光源的亮度**，色度信息保存在Cr（**红色分量**） 和Cb（**蓝色分量**） 中。



#### 4.1.3 HSV 

RGB是从硬件的角度提出的颜色模型，与人眼匹配的过程中存在一定的差异。

HSV是一种面向视觉感知系统的颜色模型。



……接下来的颜色空间不一一介绍。



### 4.2 类型转换函数

##### 1.cv2.cvtColor() :  实现以上色彩空间的变换。

```python
dst = cv2.cvtColor(src,code[,dstCn])
```

- dst ： 输出图像，与原始输入图像具有同样的数据类型和深度。
- src :  原数输入图像。可以是8位无符号图像、16位无符号图像等等。
- code ： 色彩空间转换码 。 例如 cv2.COLOR_RGB2BGR
- dstCn :  目标图像的通道数。如果参数为默认的0，则通道数自动通过原始输入图像和code得到。

### 4.3 类型转换实例

介绍几种常用的色彩空间转换。

### 4.4 HSV色彩空间讨论

略。

### 4.5 alpha通道

在RGB的基础上加A通道，即RGBA，A通道表示透明度。 PNG图像是典型的4通道图像，alpha通道的幅值范围是[0,1] , 或者 [0,255] , 表示从透明到不透明。





## 第5章 几何变换

![image-20201108162127047](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108162127047.png)

​                                                        ![image-20201108162140993](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108162140993.png)   



**知识点把握：**

几何变换是指将一副图像  **映射**  到另外一副图像内的操作。

根据OpenCV函数的不同，将映射关系分为缩放、旋转、仿射变换、透视、重映射等。

### 5.1 缩放

##### 1.cv2.resize() : 实现对图像的缩放。

```python
dst = cv2.resize(src,dsize [,fx[,fy[,interpolation]]] )
```

- dst : 输出的目标图像
- src : 原始图像
- dsize ：输出图像大小
- fx : 水平方向的缩放比例
- fy：垂直方向的缩放比例
- interpolation ： 插值方式

### 5.2 翻转

##### 1.cv2.flip() :  实现图像在水平方向翻转、垂直方向翻转、两个方向同时翻转。

```python
dst = cv2.flip(src,flipCode)
```

- flipCode : 代表旋转的类型。

  ![image-20201108165442138](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201108165442138.png)





### 5.3 仿射

仿射变换：图像通过一系列  **几何变换**  来实现平移、旋转等多种操作。

该变换能够保持图像的平直性和平行线。

```python
dst = cv2.warpAffine(src,M,dsize[,flags[,borderMode[,borderValue]]])
```

- M :  代表2x3的变换矩阵。使用不同的变换矩阵，可以实现不同的仿射变换。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109091638705.png" alt="image-20201109091638705" style="zoom:80%;" />



#### 5.3.1 平移

通过变换矩阵M实现将原始图像 src 转换为目标图像 dst：

dst(x,y) = src($M_{11}x+M_{12}y+M_{13}$, $M_{21}x+M_{22}y+M_{23}$ )



例如：将src右侧移动100像素，向下移动200像素：

```
dst(x,y) = src(x+100,y+200)
```

代码：

```python
height, width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1,0,x],[0,1,y]])
move = cv2.warpAffine(img,M,(width,height))
```

#### 5.3.2 旋转

使用   **cv2.warpAffine()**   对图像进行**旋转**时，可以通过函数 **cv2.getRotationMatrix2D()** 获取**转换矩阵**。

```python
retval = cv2.getRotationMatrix2D(center,angle,scale)
```

- center :  旋转的中心点
- angle :  旋转角度。正数代表逆时针，负数代表顺时针。
- scale :  变换尺度（缩放大小）

代码：

```python
height,width = img.shape[:2]
M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)
rotate = cv2.warpAffine(img,M,(width,height))
```

#### 5.3.3 更复杂的仿射变换

对于更复杂的仿射变换，OpenCV提供了 **cv2.getAffineTransform()** 来生成仿射函数  **cv2.warpAffine()**  所使用的的转换矩阵M。

可以将矩阵映射为任意平行四边形。

```python
retval = cv2.getAffineTransform(src,dst)
```

- src :  输入图像的三个点坐标
- dst :  输出图像的三个点坐标

![image-20201109094815505](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109094815505.png)

- retval ： 从src $\rightarrow$ dst ， 所需要的变换矩阵。

代码：

```python
rows,clos,ch = img.shape
p1 = np.float32([[0,0],[clos-1,0],[0,rows-1]])
p2 = np.float32([[0,rows*0.33],[clos*0.85,rows*0.25],[clos*0.15,rows*0.7]])
M = cv2.getAffineTransform(p1,p2)
dst = cv2.warpAffine(img , M,(clos,rows))
```

### 5.4 透视

**仿射变换**    将矩形映射为     **任意平行四边形**。

**透视变换**    可以将矩阵映射为    **任意四边形**  。

```python
dst = cv2.warpPerspective(src,M,dsize[,flags[,borderMode[,borderValue]]])
```

- dst : 输出图像。和原图像具有相同的类型。dsize决定输出图像的实际大小。
- src :  输入图像
- M :  3x3变换矩阵
- dsize :  输出图像的尺寸大小
- flags:  插值方法
- borderMode : 边类型
- borderValue: 边界值，默认为 0 。

在使用   **cv2.warpPerspective()**    之前，可以使用另一个函数    **cv2.getPerspectiveTransform()**    来生成 **转换矩阵**。

```python
retval = cv2.getPerspectiveTransform(src,dst)
```

- src   : 输入图像的四个顶点坐标
- dst ：输出图像的四个顶点坐标

与仿射变换不同，这里的两个参数都是包含4个点的数组。

代码：

```python
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,clos-50],[rows-50,clos-50]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(clos,rows))
```





### 5.5 重映射

**重映射：** 把一副图像内的像素点放置到另外一副图像内的指定位置，这个过程称为    **重映射**   。

cv2.remap() : 

```python
dst = cv2.remap(src,map1,map2,interpolation[,borderMode[,borderValue]])
```

- map1 :  有两种可能的值：

1.  表示（x,y）点的一个映射。
2. 表示CV_16SC2  ,  CV_32FC1 , CV_32FC2 类型（x,y）点的x值。

- map2 ：与map1对应的有两种值。

1. map1表示（x,y）时，该值为空。
2. 当map1表示（x，y）点的x值时，该值是CV_16SC2  ,  CV_32FC1 类型（x，y）点的y值。

#### 5.5.1 映射参数的理解

#### 5.5.2 复制

#### 5.5.3 绕x轴旋转

#### 5.5.4 绕y轴旋转

#### 5.5.5 绕x轴、y轴旋转 

#### 5.5.6 x轴、y轴互换

#### 5.5.7 图像缩放





## 第6章 阈值处理

![image-20201109102745585](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109102745585.png)

**阈值处理** ：     **剔除 **    图像内像素值    **高于一定值**   或   **低于一定值**   的像素点。

OpenCV提供了   **cv2.threshold()**    和  **cv2.adaptiveThreshold()**   ,用于实现阈值处理。



### 6.1 threshold函数

cv3.0 使用      **cv2.threshold(src,thresh,maxval,type)**    函数进行**阈值化处理** ：

```python
retval,dst = cv2.threshold(src,thresh,maxval,type)
```

- retval : 返回的阈值。
- dst ： 阈值分割结果图像。
- thresh : 设定的阈值。
- maxval ： 当type参数为THRESH_BINARY 或者 THRESH_BINARY_INV类型时，需要设定的最大值。
- type ： 阈值分割的类型。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109103722714.png" alt="image-20201109103722714" style="zoom:80%;" />

#### 6.1.1 二值化阈值处理（cv2.THRESH_BINARY）

cv2.THRESH_BINARY  : 将原始图像处理为仅有两个值的二值图像。

![image-20201109104201625](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109104201625.png)

- 灰度值 > thresh : 将灰度值设定为最大值。
- 灰度值 ≤ thresh：将灰度值设定为 0。

![image-20201109105029639](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105029639.png)



#### 6.1.2 反二值化阈值处理（cv2.THRESH_BINARY_INV）

与上相反。

![image-20201109105128009](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105128009.png)

- 灰度值 > thresh : 将灰度值设定为0。
- 灰度值 ≤ thresh：将灰度值设定为最大值。

![image-20201109105216613](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105216613.png)



#### 6.1.3 截断阈值化处理（cv2.THRESH_TRUNC）

cv2.THRESH_TRUNC：将图像中大于阈值的像素点的值设为阈值，小于或等于该阈值的像素点的值保持不变。

![image-20201109105346125](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105346125.png)

- 灰度值 > thresh :  灰度值=thresh
- 灰度值 ≤ thresh：灰度值=0

![image-20201109105442987](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105442987.png)



#### 6.1.4 超阈值零处理（cv2.THRESH_TOZERO_INV）

![image-20201109105504106](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105504106.png)

#### 6.1.5 低阈值零处理（cv2.THRESH_TOZERO）

![image-20201109105552651](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109105552651.png)



### 6.2 自适应阈值处理

**色彩均衡图像**  ，直接使用一个阈值就能完成对图像的阈值化处理。

对于     **色彩不均衡的图像**   ，只使用一个阈值，无法得到清晰有效的阈值分割结果图像。



**自适应阈值处理**：使用变化的阈值完成对图像的阈值处理。

**cv2.adaptiveThreshold()** ： 计算每个像素点周围邻近区域的加权平均获得阈值，并使用该阈值对当前像素点进行处理。自适应阈值能较好地处理明暗差异大的图像。

```python
dst = cv2.adaptiveThreshold(src,maxValue , adaptiveMethod , thresholdType , blockSize , C)
```

- src : 必须为8位单通道的图像。
- maxValue ： 最大值
- adaptiveMethod ： 自适应方法。cv2.ADAPTIVE_THRESH_MEAN_C 和cv2.ADAPTIVE_THRESH_GUASSIAN_C 。
- thresholdType ： 阈值处理方式，该值必须是 cv2.THRESH_BINARY 或者 cv2.THRESH_BINARY_INV中的一个。
- blockSize ： 块大小。表示一个像素在计算其阈值时所使用的领域尺寸，通常为 3、5、7等。
- C ： 常量

cv2.ADAPTIVE_THRESH_MEAN_C：邻域所有像素点的权重值是一致的。

cv2.ADAPTIVE_THRESH_GUASSIAN_C：与邻域各个像素点到中心点的距离有关，通过高斯方程得到各个点的权重值。



### 6.3 Otsu处理

使用 cv2.threshold() 进行处理时，需要自定义一个阈值，但一般阈值不太好找喔。

Otsu方法能够根据当前图像给出最佳的类间分割阈值。即Otus方法会遍历所有可能阈值，从而找出最佳阈值。

通过在 cv2.threshold() 中对参数type 的类型多传递一个参数 "cv2.THRESH_OTSU", 即可实现Otus方法的阈值分割。

注意：使用Otus方法时，需要将阈值设置为0.此时的  cv2.threshold()  会自动寻找最优阈值，并将该阈值返回。

```python
t,otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```

- 参数type增加了一个参数值 “cv2.THRESH_OTSU‘
- 设定的阈值为0
- 返回值t 是Otsu方法计算得到并使用的最优阈值。

ps：如果采用普通的阈值分割，返回的阈值就是设定的阈值。



## 第7章 图像平滑处理

![image-20201109114731335](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109114731335.png)

![image-20201109114742968](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109114742968.png)

**知识点把握：**

**图像平滑处理：**在尽量保留原有信息的情况下，过滤掉图像内部的噪声。所得的图像称为平滑图像。

**图像平滑处理**   会对与周围像素值  **差异极大**  的  **像素点**   进行处理，将其值调整为周围像素点像素值的   **近似值**。

**图像平滑处理的基本原理：** 将   **噪声所在像素点的像素值**    处理为    **其周围临近像素点的值**   的   **近似值**。

根据取近似值的方法，本章主要介绍：

- 均值滤波
- 方框滤波
- 高斯滤波
- 中值滤波
- 双边滤波
- 2D卷积（自定义滤波）



图像平滑处理  ===   图像模糊处理   Blurring Images

图像平滑处理  ===   图像滤波  Images Filtering



### 7.1 均值滤波

##### 7.1.1 基本原理：

使用当前像素点周围     **N*N**    个像素值的均值来代替  当前像素值。需要遍历处理图像内的每一个像素点。

- 例如 对像素点5x5区域内求均值滤波： 

​                                                    <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109171853235.png" alt="image-20201109171853235" style="zoom:50%;" /><img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109171906489.png" alt="image-20201109171906489" style="zoom: 67%;" />

- 针对边缘像素点，可以只取图像内存在的周围邻域点的像素值均值。

- 可以简化为以下形式：![image-20201109175439132](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109175439132.png)

  M和N分别对应高度和宽度。

##### 7.1.2  cv2.blur() :  均值滤波

```python
dst = cv2.blur(src,ksize,anchor,borderType)
```

- ksize :  滤波核的大小。
- anchor： 锚点，默认值是（-1，-1），表示当前计算均值的点位于核的中心点位置。使用默认值即可。
- borderType：边界样式。使用默认值即可。

### 7.2 方框滤波

##### 7.2.1 基本原理

方框滤波与均值滤波不同的是，可以自由选择滤波结果是邻域像素值之和的平均值，还是邻域像素值之和。

##### 7.2.2 cv2.boxFilter() : 方框滤波

```python
dst = cv2.boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
```

- normalize 表示在滤波时是否进行归一化处理。

1. normalize=1 ：表示要进行归一化处理，用邻域像素值的和除以面积
2. normalize=0 ： 不需要进行归一化处理，直接使用邻域像素值的和。

### 7.3 高斯滤波

##### 7.3.1 基本原理

均值滤波和方框滤波中，其邻域内每个像素的权重是相等的。

在高斯滤波中，会将中心点的权重值加大，远离中心点的权重值减小。在此基础上计算邻域内各个像素值不用权重的和。

即使用不同的   **卷积核**。

每一种尺寸的卷积核都可以有多种不同形式的权重比例。



##### 7.3.2 cv2.GussianBlur() : 高斯滤波

```python
dst = cv2.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
```

- ksize :  高斯滤波核的值必须是    **奇数**。
- sigmaX ： 卷积核在水平方向上的标准差，其控制的是权重比例。

​       例如如下sigmaX控制的不同卷积核，它们在水平方向上的标准差不同。<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109204117584.png" alt="image-20201109204117584" style="zoom:67%;" />

- sigmaY： 卷积核在垂直方向上的标准差。如果sigmaY=0，只采用sigmaX；如果sigmaX=sigmaY=0，则通过 ksize.width 和 ksize.height 得到。

1. sigmaX = 0.3 x [(ksize.width-1) x 0.5 -1] + 0.8
2. sigmaY = 0.3 x [(ksize.height-1) x 0.5 -1] + 0.8

### 7.4 中值滤波

##### 7.4.1 基本原理

中值滤波：用邻域内所有像素值的中间值来替代当前像素点的像素值。

##### 7.4.2 cv2.medianBlur(src , ksize)

```python
dst = cv2.medianBlur(src, ksize)
```

### 7.5 双边滤波

##### 7.5.1 基本原理

- 在均值、方框、高斯滤波中，计算边缘上像素点时，都会模糊边缘信息。

- 双边滤波综合考虑 **空间信息** 和 **色彩信息** 的滤波方式。
- 双边滤波不仅考虑距离信息（距离越远，权重越小），还考虑色彩信息（色彩差别越大，权重越小）。
- 双边滤波即能有效地去除噪声，又能较好地保护边缘信息。

##### 7.5.2 cv2.bilateralFilter() : 双边滤波

```python
dst = cv2.bilateralFilter(src, d,sigmaColor,sigmaSpace,borderType)
```

- d : 在滤波时选取的空间距离参数，这里表示   **以当前像素点为中心点的直径**   。实时应用时推荐 d = 5，较大的离线噪声可以选择 d= 9.
- sigmaColor :  与当前像素点的像素值差值小于sigmaColor的像素点，能够参与到当前的滤波中。
- sigmaSpace ： 坐标空间中的sigma值。 一般令 sigmaSpace = sigmaColor，如果它们的值比较小（例如小于10），滤波效果不明显；较大（大于150），产生卡通效果。

### 7.6 2D卷积（自定义滤波）

##### 1.cv2.filter2D() : 自定义卷积核实现卷积操作

```python
dst = cv2.filter2D(src,ddepth,kernel,anchor[,delta],borderType)
```

- src ： 原始图像。图像深度是 CV_8U 、CV_16U 、CV_16S、CV_32F或者CV_64F中的一种。
- ddepth : 处理结果图像的图像深度，一般使用-1表示与原始图像使用相同的图像深度。
- delta : 修正值。在基础滤波的结果上加上该值，作为最终的滤波处理结果。



## 第8章 形态学操作

![image-20201109211802116](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109211802116.png)

**知识点把握：**

- 形态学主要从图像内提取    **分量信息**  ，该分量信息通常对于表达和描绘  **图像的形状**  具有重要意义。
- 形态学操作： 腐蚀、膨胀、开运算、闭运算、形态学梯度运算、顶帽运算、黑帽运算等操作。
- 形态学操作一般作用于   **二值图** ，来连接   **相邻**   的元素或   **分离**   成独立的元素。
- 腐蚀 + 膨胀  $\longrightarrow$  形态学运算的基础
- 腐蚀 + 膨胀  $\longrightarrow$  实现开运算、闭运算、形态学梯度运算、顶帽运算、黑帽运算等不同形式的运算。



**基础：**  

腐蚀和膨胀原理概述：

- 从数学来讲，膨胀或腐蚀就是将   **图像A**   与   **核B**   进行       **卷积**  。

1.  核 ： 可以是任何的形状和大小，它拥有一个单独定义的参考点，称为锚点（anchor）。
2. 核 ： 多数情况下，核是一个小的    **中间带参考点**    的     **正方形或圆盘**。

- 膨胀 ： 锚点像素值 == 核覆盖的**局部最大值**
- 腐蚀 ： 锚点像素值 == 核覆盖的**局部最小值**

### 8.1 腐蚀（变瘦）

#### 8.1.1基本原理

- 腐蚀能将图像的  **边界点消除**，以致边界向内收缩。 也可以将小于    **指定结构体元素**    的部分去掉。
- 腐蚀用来 “收缩” 或 “细化”二值图像中的前景，实现  **去除噪声 、 元素分割**    等功能。
- 腐蚀过程中， 使用一个  **结构元**   来逐个像素地扫描  **要被腐蚀的对象** 。 并根据 **结构元** 和    **被腐蚀图像**    的关系来确定    **腐蚀结果**。

**例如：** 下图表示 **结构元** 与   **前景色**   的两种不同关系。

![image-20201109215604897](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201109215604897.png)

- 左图：**结构元**  完全在 **前景图像** 中， 将  **结构元中心点**  所对应的  **腐蚀结果图像dst**  中的像素点处理为  **前景色（白色）**  。
- 右图：**结构元**  部分在 **前景图像** 中， 将  **结构元中心点**  所对应的  **腐蚀结果图像dst**  中的像素点处理为  **背景色（黑色）**  。



#### 8.1.2 cv2.erode() : 腐蚀操作

```python
dst = cv2.erode(src,kernel [,anchor[,iterations [,borderType [,borderValue]]]])
```

- kernel : 代表腐蚀操作时所采用的结构类型。它可以自定义生成，也可以通过函数    **cv2.getStructuringElement()**  生成。
- anchor ： 同上
- iterations ： 腐蚀操作迭代的次数。

使用更大的核、更多的迭代次数，图像会被腐蚀得更严重。





### 8.2 膨胀

#### 8.2.1 基本原理

- 扩大ROI，感兴趣区域变大

#### 8.2.2 cv2.dilate() :  膨胀

```python
dst = cv2.dilate(src,kernel [,anchor[,iterations[,borderType[,borderValue]]]])
```

- kernel : 膨胀操作所采用的数据结构类型。它可以自定义生成，也可以通过函数 cv2.getStructuringElement() 生成。



### 8.3 通用形态学函数

#### 8.3.1 cv2.morphologyEx() :  将膨胀与腐蚀各种组合，实现形态学的各种运算。

```python
dst = cv2.morphologyEx(src,op, kernel [,anchor[,iterations[,borderType[,borderValue]]]])
```

- op :  操作类型。 各种形态学运算的操作规则均是将腐蚀和膨胀等操作进行组合而得到的。

![image-20201110092744651](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110092744651.png)

- 参数kernel 、anchor、iterations、borderType、borderValue与函数 cv2.erode()内相应参数的含义一致。



### 8.4 开运算

#### 8.4.1 基本原理

- 先将图像腐蚀，再对腐蚀的结果进行膨胀。 dilate( erode(src) )
- 开运算作用：能够去除孤立的小点、毛刺和小桥。

#### 8.4.2 cv2.MORPH_OPEN

```python
openimg = cv2.morphologyEx(img , cv2.MORPH_OPEN , kernel)
```

![image-20201110094322391](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110094322391.png)

![image-20201110094335641](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110094335641.png)

### 8.5 闭运算

#### 8.5.1 基本原理

- 先将图像膨胀，再对膨胀的结果进行腐蚀。 eroade(dilate(src))
- 闭运算作用：填平前景图像的小孔，弥合一些小裂缝，保持总的位置和形状不变。

#### 8.5.2 cv2.MORPH_CLOSE

```python
openimg = cv2.morphologyEx(img , cv2.MORPH_CLOSE , kernel)
```

![image-20201110094354786](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110094354786.png)

![image-20201110094409787](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110094409787.png)



### 8.6 形态学梯度运算

#### 8.6.1基本原理

- 用图像的    **膨胀图像**  减  **腐蚀图像**   的操作，该操作可以获取原始图像中前景图像的  **边缘**。
- 形态学梯度运算演示：

![image-20201110100436393](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110100436393.png)

#### 8.6.2 cv2.MORPH_GRADIENT

```python
dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
```

![image-20201110101123081](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110101123081.png)



### 8.7 礼帽运算

#### 8.7.1 基本原理

- 用原始图像减去其开运算图像的操作
- 礼帽运算的作用：获取图像ROI外部的噪声信息，或者得到比原始图像的边缘更亮的边缘信息。

![image-20201110101520232](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110101520232.png)

#### 8.7.2 cv2.MORPH_TOPHAT

```
dst = cv2.morphologyEx(img,cv2.MORPH_TOPHAT)
```



### 8.8 黑帽运算

#### 8.8.1 基本原理

- 用闭运算图像减去原始图像的操作
- 黑帽运算的作用： 能获取图像ROI内部的噪声，或的带比原始图像边缘更暗的边缘部分。

![image-20201110102950564](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110102950564.png)

#### 8.8.2 cv2.MORPH_BLACKHAT

```python
result = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) 
```



### 8.9 核函数

#### 8.9.1 基本原理

- 进行形态学操作时，必须使用一个特定的 **核** 。该核可以自定义生成，也可以通过 **cv2.getStructuringElement()** 构造。
- **cv2.getStructuringElement()** 能够构造并返回一个用于形态学处理所使用的的 **核** 。

#### 8.9.2 cv2.getStructuringElement()

```python
dst = cv2.getStructuringElement(shape,ksize[,anchor])
```

- shpe :  核形状类型。

![image-20201110104433890](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110104433890.png)

- ksize :  核 的大小。
- anchor ： 核 中定义的锚点位置。默认的值是（-1，-1），是形状的中心。



# 第9章 图像梯度

![image-20201110104646107](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110104646107.png)

**知识点把握：**

- 图像梯度计算的是图像变化的速度。

  1. 对于图像的   **边缘部分** ：其灰度值变化较大，梯度值也大； 

  2. 对于图像的   **平滑部分** ：其灰度值变化小，相应的梯度值也小。

-  图像梯度计算需要求  **导数** ，但是图像梯度一般通过计算  **像素值的差**  来得到   **梯度的近似值**  （近似导数值）。

- 将上述运算关系进一步优化，可以得到更复杂的边缘信息。本章关注3种算子掌握。
  1.  Sobel 算子
  2. Scharr算子
  3. Laplacian算子



## 9.1 Sobel理论基础

#### 9.1.1 基本理论

- 关于Sobel算子？
  1. 一种离散的微分算子，结合了   **高斯平滑**   和   **微分求导**   运算。
  2. Sobel算子利用局部差分寻找边缘，计算得到的是  **梯度的近似值**。
- 关于滤波器？
  1. 本章所说的  **“Sobel算子”**  通常是指 **“Sobel滤波器”**  。
  2. 滤波器是信号邻域的称呼，数学领域将其称为    **“核”**  。
  3. **线性核**： 即滤波的     **目标像素点的值**   等于     **原始像素值 ** 及其   **周围像素值**   的  **加权和**。
  4. 基于   **线性核**   的滤波器，就是    **卷积**。



#### 9.1.2 计算   水平+垂直 方向偏导数的近似值

##### 1.Sobel算子计算公式：

![image-20201110161223573](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110161223573.png)

- $G_x、G_y$ 分别代表    **横向**   和   **纵向**   边缘检测的 图像灰度值。

- A ： 原始图像

- Sobel 横向和纵向的 算子（卷积因子）如下：

  ![image-20201110161759611](file://C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20201110161759611.png?lastModify=1604996827)

  

##### 2.具体计算如下：

$$
Gx = (-1)*f(x-1, y-1) + 0*f(x,y-1) + 1*f(x+1,y-1)

      +(-2)*f(x-1,y) + 0*f(x,y)+2*f(x+1,y)

      +(-1)*f(x-1,y+1) + 0*f(x,y+1) + 1*f(x+1,y+1)  \\
  = [f(x+1,y-1)+2*f(x+1,y)+f(x+1,y+1)]-[f(x-1,y-1)+2*f(x-1,y)+f(x-1,y+1)]    
      
$$

$$
Gy =1* f(x-1, y-1) + 2*f(x,y-1)+ 1*f(x+1,y-1)+0*f(x-1,y) 0*f(x,y) + 0*f(x+1,y)+(-1)*f(x-1,y+1) + (-2)*f(x,y+1) + (-1)*f(x+1, y+1)  \\
= [f(x-1,y-1) + 2f(x,y-1) + f(x+1,y-1)]-[f(x-1, y+1) + 2*f(x,y+1)+f(x+1,y+1)]
$$

G 为  $f(x,y)$ 该点像素值的大小。
$$
G=\sqrt{G_x^2 + G_y^2}
$$

##### 3.用以下公式计算梯度方向：

![image-20201110163123197](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163123197.png)

##### 4.简化

**水平方向偏导数计算**：

![image-20201110163315526](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163315526.png)

​                                                                                              ![image-20201110163329853](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163329853.png)

**垂直方向偏导数计算**：

![image-20201110163412402](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163412402.png)

![image-20201110163423761](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163423761.png)





## 9.2 Sobel 算子及函数使用

### 1.cv2.Sobel() : 实现Sobel算子运算

```python
dst = cv2.Sobel(src,ddepth,dx,dy[,ksize[,scale[,delta[,borderType]]]])
```

- ddepth 代表输出图像的深度。

![image-20201110163659072](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110163659072.png)

- dx ： x方向上的求导阶数
- dy ： y方向上的求导阶数
- ksize ： Sobel核的大小。该值为 -1时，会使用Scharr算子进行运算。
- delta ： 加在目标图像dst上的值。

### 2.参数 ddepth

- 在实际操作中，计算梯度值可能会出现负数。

- 通常处理的图像是8位图类型，如果结果图像也是8位图，那么负数会自动截断为 0，发生信息丢失。
- 为了避免信息丢失，计算时我们使用更高的数据类型 cv2.CV_64F, 再通过取绝对值将其映射为 cv2.CV_8U（8位图）类型。

OpenCV中，使用 cv2.convertScaleAbs() 对参数取绝对值。

```python
dst = cv2.convertScaleAbs(src [,alpha[,beta]])
```

- alpha :  调节系数，默认为1。
- beta ：调节亮度值，默认为0 。
- 作用：将原始图像装换为256色位图    

```python
dst = saturate(src*aipha+beta)      #saturate()表示计算结果的最大值是饱和值
```

### 3.方向dx、dy

参数dx 和 dy 包含多种形式的组合：

- 计算x方向边缘（梯度）： dx = 1 , dy = 0

![image-20201110170804865](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110170804865.png)





- 计算y方向边缘（梯度）： dx = 0 , dy = 1

![image-20201110170823141](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110170823141.png)

- 获取两个方向上的边缘信息：dx = 1 , dy = 1

![image-20201110171008008](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110171008008.png)

- 计算x方向和y方向的边缘叠加

![image-20201110171021743](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110171021743.png)

## 9.3 Scharr算子及函数使用

##### 9.3.1 Scharr算子的核：

![image-20201110171927423](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110171927423.png)

##### 9.3.2 cv2.Scharr() : 计算Scharr算子

```python
dst = cv2.Scharr(src,ddepth,dx,dy[,scale[,delta[,borderType]]])
```



## 9.4 Sobel算子和Scharr算子的比较

Sobel算子缺点：当其核结构较小时，精确度不高。Scharr算子相对具有更高的精度。

## 9.5 Laplacian算子及函数使用

#### 9.5.1 基本简介

- Laplacian算子是一种二阶导数算子，其具有  **旋转不变性**，  可以满足不同方向的图像边缘锐化（**边缘检测**）要求。

- 通常情况下，其算子的系数之和需要为 0。

- 例如：![image-20201110173521402](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110173521402.png)

  ```python
  dst = cv2.Laplacian(src,ddepth[,ksize[,scale[,delta[,borderType]]]])
  ```

  - ksize : 计算二阶导数的核尺寸大小，该值必须是正的奇数。
  - scale ： Laplacian值的缩放比例。默认为 1 。

## 9.6 算子总结

Sobel、Scharr、Laplacian算子都可以用作边缘检测。如下图：

![image-20201110174238867](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110174238867.png)

- Sobel、Scharr 计算的是一阶近似导数的值。

![image-20201110174326495](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110174326495.png)

- Laplacian计算的是二阶近似导数的值。

![image-20201110174401842](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110174401842.png)



# 第10章 Canny边缘检测

![image-20201110174602230](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110174602230.png)

![image-20201110174616459](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110174616459.png)

**知识点把握：**

Canny边缘检测是一种  使用**多级边缘检测**算法 检测边缘的方法。

- Canny 边缘检测步骤：
  1. 去噪。 噪声会影响边缘检测的准确性，因此首先就要过滤掉噪声。
  2. 计算梯度的幅度与方向。
  3. 非极大值抑制，即适当地让边缘 “变瘦” 。
  4. 确定边缘。 使用双阈值算法确定最终的边缘信息。

10.1 将对Canny检测的几个步骤分别进行简单的介绍。

## 10.1 Canny边缘检测基础

#### 10.1.1 应用高斯滤波去除图像噪声

- 图像边缘易受噪声干扰，避免检测到错的边缘，需要对图像进行滤波去除噪声。
- 滤波能平滑一些纹理较弱的非边缘区域。
- 实际处理中，通常采用高斯滤波去除图像中的噪声。
- 高斯滤波器：越临近中心的点，权重越大。总体权值和 == 1 。

具体操作见 **第7章 图像平滑处理**  。

#### 10.1.2 计算梯度

- 梯度包含两个特性： **幅度** + **方向** 。
- **第九章 图像锐化**  用到梯度的  **幅度**  。canny这我们关心梯度的   **方向**  。梯**度的方向**  与  **边缘的方向**   是  **垂直的**。

**边缘检测算子中的梯度**：

边缘检测算子返回水平方向的 $G_x$ 和垂直方向的 $G_y$ 。梯度的   **幅度G**   和  **方向 $\theta$** (用角度值表示)为：

![image-20201110203549827](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110203549827.png)

- 梯度总与边缘垂直。通常会有8个不同方向（东西南北等）。
- 梯度的可视化表示法：

![image-20201110203809618](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110203809618.png)



#### 10.1.3 非极大值抑制

**非极大抑制**： 获得梯度的  **幅度和方向**  后，**遍历**  图像中的像素点，**去除**  所有非边缘的点。

**具体实现**：

​       逐一遍历像素点，判断   **当前像素点**   是否是   **周围像素点中**   **具有相同梯度方向**    的    **最大值**。

- 如果该点是  **正/负梯度**   方向上的局部最大值，则保留该点。
- 如果不是，则抑制该点。

周围像素点：可能是4邻域？

![image-20201110205142175](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110205142175.png)

正/负梯度：只是指方向，值都是绝对值化后的？

![image-20201110205152308](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110205152308.png)

#### 10.1.4 应用双阈值确定边缘

完成上述步骤后，图像的强边缘已经在当前获取的边缘图像内。

但是，一些虚边缘可能在真实图像内，例如由真实图像内部产生的虚边缘。也有可能是噪声，噪声必须剔除。

**具体实现**：

​        设置两个阈值： maxVal 和 minVal 。 根据当前边缘像素的   **梯度幅度**  与这两个阈值之间的关系，来判断边缘的属性。步骤如下：

              1.   当前像素值梯度幅度  ≥  maxVal    ：   强边缘 。
                 2.     minVal ＜ 当前像素值梯度幅度 ＜maxVal   ：  虚边缘 （需要保留）。
                 3.     当前像素值梯度幅度  ≤  minVal  ： 抑制当前边缘像素。

​         得到虚边缘，对虚边缘进一步处理 ： 判断虚边缘与墙边缘是否连接，来确定虚边缘到底属于哪种情况。

1. 与强边缘连接 ：  边缘。
2. 无连接  ：  抑制。

![image-20201110210847892](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110210847892.png)

**A** ： 大于maxVal，A是强边缘。

**B**  :    介于 minVal 和  maxVal之间，与强边缘连接，保留。

**C** ：  介于 minVal 和  maxVal之间 ，与强边缘不连接，抑制。

**D** ： 抑制。

## 10.2 Canny函数及使用

#### 1.cv2.Canny() : 实现Canny边缘检测。

```python
edges = cv2.Canny(image,threshold1, threshold2 [,apertureSize[,L2gradient]])
```

- image : 8 位
- threshold1 ： minValue
- threshold2 ： maxValue
- apertureSize ： Sobel算子孔径的大小。
- L2gradient ： 计算图像梯度幅度的标识 。默认值为False（L1范数）。如果为True（L2范数）。





# 第11章 图像金字塔

![image-20201110213316841](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110213316841.png)

**知识点把握：**

图像金字塔： 一副图像的多个不同分辨率的子图所构成的图像集合。

- 这组图像是有 **原始图像** 不停   **降采样**  至一个像素点来获得。

- 金字塔最底部是 **原始图像** ，通常情况下，每向上移动一级，图像的宽和高都降低为原来的  **二分之一**。

![image-20201110214117808](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110214117808.png)



## 11.1 理论基础

**最简单的图像金字塔**： 通过不断地删除图像的  **偶数行**和**偶数列**  获得。

**经过滤波的金字塔**： 先对原始图像  **滤波**，得到原始图像的  **近似图像**， 再将近似图像的偶数行和偶数列删除以获取 **下采样**  的结果。

- 滤波器有多种可以选择：

  1. 邻域滤波器：采用邻域平均，得到平均金字塔。
  2. 高斯滤波器：使用高斯滤波对原始图像滤波，得到高斯金字塔。 是函数 **cv2.pyrDown()** 所采用的方式。

  **高斯金字塔产生流程**：

  ![image-20201110220434485](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110220434485.png)

  原始图像与各次向下采样所得到的结果图像共同构成了   **高斯金字塔**。

- 若上采样，对新生成的像素点进行赋值，称为插值处理。

  常见的上采样方式是对像素点以补零的方式完成插值。

  通常是在   **每列像素点的右侧**   插入值为零的列，在   **每行像素点的下方**   插入值为零的行。

  ![image-20201110222228567](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201110222228567.png)

  使用下采样时所用的   **高斯滤波器**   对   **补零后的图像**   进行滤波处理。

  此时图像中   **3/4像素点**   的值都是零，所以要将高斯滤波器系数   **乘以4**，以保证得到的像素值的范围仍旧在[0,255]内。

## 11.2 pyrDown函数及使用

#### 1.cv2.pyrDown() :  高斯金字塔操作中的下采样

```python
dst = cv2.pyrDown( src[,dstsize[,borderType]])
```

- dstsize : 目标图像的大小。 默认为  $Size( (src.cols+1)/2,(src.rows+1)/2 )$ .

## 11.3 pyrUp函数及使用

#### 1.cv2.pyrUp() :  图像金字塔中的上采样

```python
dst = cv2.pyrUp(src[,dstsize[,borderType]])
```

- dstsize : 目标图像的大小。默认为   $Size( src.cols*2,src.rows*2 )$ .

## 11.4 采样可逆性的研究

原始图像先后经过向下采样、向上采样后，所得到的结果图像与原始图像的    **大小一致**  ，看起来也相似，但它们的    **像素值不一致**  。

## 11.5 拉普拉斯金字塔

#### 1.定义

为了在上采样时能够恢复具有较高分辨率的原始图像， 就要获取在采样过程中 **所丢失的信息**，这些   **丢失的信息**   就构成了    **拉普拉斯金字塔**。

**公式表示**：
$$
L_i = G_i - pyrUp(G_i +1)
$$
​                                                                $L_i$ :  拉普拉斯金字塔中的第 $i$ 层

​                                                                $G_i$ :  高斯金字塔中的第 $i$ 层



​                                                 ![image-20201111152604799](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111152604799.png)

#### 2.应用

**laplacian金字塔作用**： 能够恢复高分辨率的图像。

![image-20201111153851590](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111153851590.png)



# 第12章 图像轮廓

![image-20201111155605654](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111155605654.png)

​                                                    ![image-20201111155638755](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111155638755.png)   

**知识点把握：**

- 边缘检测出的边缘是    **不连续**  的。
- 图像轮廓是指将边缘连接形成一个   **整体**。
- **cv2.findContours()** : 查找图像内的轮廓信息。
- **cv2.drawContours()** : 将轮廓绘制出来。
- 通过对轮廓的操作，能够获取目标图像的大小、位置、方向等信息。

## 12.1 查找并绘制轮廓

### 12.1.1 cv2.findContours() : 查找图像轮廓

```python
image, contours, hierarchy = cv2.findContours( image, mode, method)
```

**返回值**：

- image :  与函数参数中的原始图像image一致。
- contours：返回的轮廓。
- hierarchy：图像的拓扑信息（轮廓层次）。

**参数**：

- image：原始图像，8位。所有非零值被处理为1，零值保持不变。即会将   **灰度图**   转为   **二值图**。
- mode ：轮廓检索模式。
- method：轮廓的近似方法。



**返回值系列：**

##### 1.返回值 iamge

OpenCV 4.X已被取消，函数 cv2.findContours()仅有两个返回值。

```python
contours,hierarchy = cv2.findContours( image,mode,method)
```



##### 2.返回值 contours

contours = list[ numpy.nadarry1,  numpy.nadarry2,  numpy.nadarry3, ..... ]

每个numpy.nadarry 都是一个轮廓，**每个轮廓**  都对应着   **一系列的点** 。每个点都是一个坐标。



##### 3.返回值 hierarchy

描述轮廓之间的关系，外部的轮廓称为   **父轮廓**，  **父轮廓内部 **   的轮廓叫做  **子轮廓**。

每个轮廓 contours[i] 对应  **4个元素**  来说明当前轮廓的   **层次关系**。

- Next ： 后一个轮廓的索引编号。
- Previous ：前一个轮廓的索引编号。
- First_Child : 第1个子轮廓的索引编号
- Parent ： 父轮廓的索引编号。



**参数系列：**

##### 1.参数iamge

- 输入图像，必须是8位单通道二值图。
- 一般都是将图像处理为二值图后，再将其作为image参数使用。



##### 2.参数mode

参数mode决定轮廓的提取方式，具体有4种：

- **cv2.RETR_EXTERNAL** :  只检测外轮廓<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111165014505.png" alt="image-20201111165014505" style="zoom:50%;" />

- **cv2.RETR_LIST** :   对检测到的轮廓不建立等级关系<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111165037858.png" alt="image-20201111165037858" style="zoom:50%;" />
- **cv2.RETER_CCOMP** :  检索所有轮廓并将它们组织成两级层次结构。<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111165054022.png" alt="image-20201111165054022" style="zoom:50%;" />
- **cv2.RETR_TREE** :  建立一个等级树结构的轮廓。<img src="file://C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20201111165054022.png?lastModify=1605084709" alt="image-20201111165054022" style="zoom:50%;" />

##### 3.参数method

method决定了如何表达轮廓。

- cv2.CHAIN_APPROX_NONE ： 存储所有的轮廓点，相邻两个点的像素位置不超过 1 。即$max(abs(x_1-x_2),abs(y_2-y_1)) = 1$
- cv2.CHAIN_APPROX_SIMPLE :  只保留某方向上的终点坐标，例如 一个矩形只需要用4个点。
- cv2.CHAIN_APPROX_TC89_L1 :
- cv2.CHAIN_APPROX_TC89_KCOS :



##### **使用cv2.findContours()需要注意**

- 待处理的图像必须是灰度二值图
- 在OpenCV中，都是从黑色背景中找白色对象。因此，对象必须是白色，背景必须是黑色。
- 在OpenCV 4.x中，函数cv2.findContours()仅有两个返回值。



### 12.1.2 cv2.drawContours() : 绘制图像轮廓

```python
image = cv2.drawContours( 
                          image, contours, contourIdx, color
                           [,thickness [,lineType [, hierarchy[,maxLevel[,offset]]]]])
```

- image : 待绘制轮廓的图像。 函数会在image上直接绘制轮廓。

- contours ： 需要绘制的轮廓。

- conttourIdx : 需要绘制的边缘索引。告诉函数需要绘制某一条轮廓还是全部轮廓（-1）。

- color ： 绘制的颜色，用BGR格式表示。

- thickness：画笔粗细

- lineType：绘制轮廓所用线型

  

也可以将cv2.drawContours() 写为没有返回值的形式。





## 12.2 矩特征

- **比较两个轮廓**   最简单的方法： 比较二者的轮廓矩。
- **轮廓矩**： 代表了一个轮廓、一副图像、一组点集的 **全局特征**。
- **矩信息**：包含了对象不同类型的几何特征，例如大小、位置、角度、形状等。
- **矩特征**   被广泛地应用在模式识别、图像识别等方面。

​      <img src="https://upload-images.jianshu.io/upload_images/14512145-7421018b85e354a1.png?imageMogr2/auto-orient/strip|imageView2/2/w/952/format/webp" alt="img" style="zoom:80%;" />                       

​          <img src="https://upload-images.jianshu.io/upload_images/14512145-0449096f20774179.png?imageMogr2/auto-orient/strip|imageView2/2/w/619/format/webp" alt="img" style="zoom:80%;" />

**参考**：   [图像的矩（含hu不变矩）](https://www.jianshu.com/p/3cb0b97da76e)



### 12.2.1 cv2.moments() : 矩的计算

```python
retval = cv2.moment( array[, binaryImage])
```

- array : 可以是点集，也可以是灰度图像或二值图。
- binaryImage :  该参数为True时，array内所有的非零值都被处理为 1 。该参数仅在参数 array 为图像时有效。
- retval ： 矩特征。主要包括：

​                      <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201111203530480.png" alt="image-20201111203530480" style="zoom:80%;" />

​                      上述矩都是根据公式计算得到的。

**零阶矩和一阶矩 **：可以计算某个形状的重心。

**二阶矩**：用来计算形状的方向。

**中心矩**：能比较不同位置的两个对象的一致性。（平移不变性）

**归一化中心矩**：考虑 **缩放后 **    大小不一致的对象 的  **一致性**。



### 12.2.2 cv2.contourArea() : 计算轮廓的面积

```python
retval = cv2.contourArea(contour[, oriented])
```

- retval ： 面积值。
- contour ： 轮廓。
- oriented ： bool值。当它为True时，返回的值包括正/负号，用来表示轮廓是顺时针还是逆时针的。默认值是false，返回的是绝对值。



### 12.2.3 cv2.arcLength() : 计算轮廓的长度。

```
dst = cv2.arcLength(curve,closed)
```

- curve : 轮廓
- closed ： 布尔值，用来表示轮廓是否封闭。该值为True时，表示轮廓是封闭的。

## 12.3 Hu矩

- **Hu矩：**归一化中心矩的线性组合，每一个都是通过归一化中心矩的组合运算得到的。
- Hu矩能保持图像旋转、缩放、平等等不变性。

### 12.3.1  cv2.HuMoments() :  根据矩特征来获得Hu矩值

```
hu = cv2.HuMoments(m)
```

- m : 由函数cv2.moments() 计算得到的矩特征。
- hu ： 返回的Hu矩。

cv2.moments()返回的归一化中心矩包括：

 ![image-20201113085206183](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201113085206183.png)



### 12.3.2 形状匹配

可以通过Hu矩来判断两个对象的一致性。

```python
retval = cv2.matchShapes(contour1, contour2, method, parameter)
```

- contour1 : 第一个轮廓或者灰度图像
- contour2 : 第二个轮廓或者灰度图像
- method ： 比较两个对象的Hu矩的方法。

![image-20201113085556440](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201113085556440.png)



结果分析：

- 同一副图像的Hu矩是不变的额，差值为0
- 相似图像即使发生平移、缩放和旋转后，cv2.matchShapes()返回的差值也较小。
- 不相似图像，差值较大。

## 12.4 轮廓拟合

计算轮廓时，仅需要一个接近于轮廓的近似多边形。

OpenCV提供了多种计算轮廓近似多边形的方法。

### 12.4.1 cv2.boundingRect() : 矩形包围框

```python
retval = cv2.boundingRect(array)
```

- **retval** : 矩形边界的左上角顶点的**坐标值**  +  矩形边界的**宽度和高度**
- array ： 灰度图像或轮廓。

```
x,y,w,h = cv2.boundingRect(array)
```

- 左上角顶点 （x,y）。

- 矩形边界的x,y长度。

### 12.4.2 cv2.minAreaRect() : 最小包围矩形框

```
retval = cv2.minAreaRect(points) 
```

- retval : 返回的矩形特征信息，结构（最小外接矩形的中心（x,y）,(w,h) , 旋转角度）
- points ： 轮廓。

retval 不符合 函数cv2.drawContours()的参数结构要求，需要使用cv2.boxPoints() 来装换。

```
points = cv2.boxPoints(box)
```

- points :  可以用于cv2.drawContours() 参数的轮廓点
- box ： cv2.minAreaRect() 返回值的类型的值。



### 12.4.3 cv2.minEnclosingCircle() : 最小包围圆

```
center, radius = cv2.minEnclosingCircle(points)
```

- center : 最小包围圆的中心
- radius ：最小包围圆的半径
- points ： 轮廓



### 12.4.4 cv2.filtEllipse()

```
retval = cv2.fitEllipse(points)
```

- retval : RotateRect类型的值。
- points ： 轮廓



### 12.4.5 cv2.fitLine() : 最优拟合直线

```
line = cv2.fitLine(points, distType, param, reps, aeps)
```

- 用的时候再琢磨



### 12.4.6  cv2.minEnclosingTriangle() :  最小外包三角形

```
retval , triangle = cv2.minEnclosingTriangle(points)
```



### 12.4.7 cv2.approxCurve() : 逼近多边形

```
approxCurve = cv2.approxPolyDP (curve, eplion, closed)
```



## 12.5 凸包

**这就是凸包：** 

![image-20201113093005456](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201113093005456.png)



### 12.5.1 cv2.convexHull() : 获取轮廓的凸包

```
hull = cv2.convexHull(points [,clockwise [,returnPoints]])
```

- points : 轮廓
- hull ： 凸包角点



### 12.5.2 cv2.convexityDefects() : 获取凸缺陷

凸缺陷： 凸包与轮廓之间的部分。

```
convexityDefects = cv2.convexityDefects(contour,convexHull)
```

- convexityDefects ：凸缺陷点集。 [起点，终点，轮廓上距离凸包最远的点，最远点到凸包的近似距离]



### 12.5.3 几何学测试

本节介绍几种与凸包有关的几何学测试。

1. ##### cv2.isContourConvex() : 测试轮廓是否是凸形的

```
retval = cv2.isContourConvex(contour)
```

##### 2.cv2.pointPolyTest() : 点到轮廓的距离

```
retval = cv2.pointPolyTest(contour,pt,measureDist)
```

## 12.6 利用形状场景算法比较轮廓

用矩比较形状是一种有效的方法，但从OpenCV3开始，有了专属模块shape，该模块中的形状场景算法能更高效地比较形状。

### 12.6.1 计算形状场景距离

### 12.6.2 计算Hausdorff距离

## 12.7 轮廓的特征值

轮廓自身的一些属性特征及轮廓所包围对象的特征对于描述图像具有重要意义。

### 12.7.1 宽高比

### 12.7.2 Extent

Extend = 轮廓面积（对象面积）/ 矩形边界面积

### 12.7.3 Solidity

solidity = 轮廓面积（对象面积）/ 凸包面积

### 12.7.4 等效直径

该值是与轮廓面积相等的圆形的面积。

![image-20201113171945255](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201113171945255.png)

### 12.7.5 方向

### 12.7.6 掩模和像素点

### 12.7.7 最大值和最小值及它们的位置

### 12.7.8 平均颜色及平均灰度

### 12.7.9 极点



# 第13章 直方图处理

![image-20201113173143345](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201113173143345.png)

## 13.1 直方图的含义

直方图中，**横坐标**    是图像中各像素点的    **灰度级**，**纵坐标 **   是具有该灰度级的   **像素个数**。

归一化直方图：x轴让仍表示灰度级， y轴表示灰度级出现的概率。

OpenCV中绘制直方图时，注意3个概念：**DIMS**、**BINS**、**RANGE**。

**DIMS**：收集参数的数量。一般情况下，只有一种，就是灰度级。

**BINS**：统计的灰度级范围。一般为  [0,255]

**RANGE**：参数子集的数目。有时需要将众多的数据划分为若干个组。例如有5个灰度级，其BINS值为5.



## 13.2 绘制直方图

- **两种方案绘制直方图**

1. python : **matplotlib.pyplot()**
2. OpenCV : **cv2.calcHist()** 

### 13.2.1 使用Numpy绘制直方图

##### 1.matplotlib.pyplot.hist() : 根据数据源和灰度级分组绘制直方图

```python
matplotlib.pyplot.hist(X,BINS)
```

- **X** :  数据源，必须是一维的。图像通常是二维的，需要使用 ravel() 函数将图像处理为一维数据源。
- **BINS** ： 表示灰度级的分组情况。



### 13.2.2 使用OpenCV绘制直方图

##### 1.cv2.calcHist()

```python
hist = cv2.calcHist(images , channels, mask, histSize, ranges, accumulate)
```

- hist : 返回的统计直方图，是一个一维数组，数组内的元素是各个灰度级的像素个数。
- images ： 原始图像，需要用 “[]”括起来
- channels : 指定通道编号
- mask ： 掩模图像
- histSize ： BINS的值，也用"[]"括起来
- ranges ：像素值范围
- accumulate : 累计标识，默认值为False。

##### 2.plot()函数：将cv2.calcHist()的返回值绘制为图像直方图

##### 3.绘制统计直方图



### 13.2.3 使用掩模绘制直方图

在cv2.calcHist()中，参数mask用于标识是否使用掩模图像。

当使用掩模图像获取直方图时，仅获取mask指定区域的直方图。

##### 1.掩模处理是怎么回事

将  **掩模图像**  看作一块玻璃板，玻璃板上的白色区域是透明的，黑色区域是不透明的。

**掩模运算**  ： 将该玻璃板覆盖在原始图像上，透过玻璃板显示出来的部分就是掩模运算的结果图像。

![image-20201114095625551](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201114095625551.png)

##### 2.如何构造掩模图像

a. 先构造一个像素值都是0的二维矩阵

b.将数组中指定区域的像素值设为255

##### 3.使用掩模绘制直方图

a. 先将函数cv2.calcHist()的mask参数设为掩模图像，得到掩模处理的直方图信息。

b. 再使用plot()函数完成直方图的绘制。

```
hist = cv2.calcHist(images, channels, mask, histSize, ranges, accumulate)
```



## 13.3 直方图均衡化

图像如果拥有全部的灰度级，并且像素值的灰度均匀分布，那么这幅图像就具有高对比度和多变的灰色色调。

**直方图均衡化目的**： 将原始图像的灰度级均匀地映射到整个灰度级范围内。

这种均衡化，既实现了  **灰度值统计**  上的   **概率均衡**，也实现了  **人类视觉系统（HVS）**   的  **视觉均衡**。



### 13.3.1 直方图均衡化原理

直方图均衡化主要包含两个步骤：

- 计算累计直方图。
- 对累计直方图进行区间转换。



具体原理可以自己查阅数字图像处理。



### 13.3.2 cv2.equalizeHist() : 实现直方图均衡化

```python
dst = cv2.equalizeHist( src ) 
```

- src :  8位单通道原始图像。
- dst ： 直方图均衡化处理的结果。



## 13.4 pyplot模块介绍

matplotlib.pyplot模块提供了一个类似于MATLAB绘图方式的框架。

### 13.4.1 subplot函数 

向当前窗口内添加一个子窗口对象。

```python
matplotlib.pyplot.subplot(nrows,ncols,index)
```

- **nrows** : 行数
- **ncols** ： 列数
- **index** ： 窗口序号

例如： subplot(2,3,4) : 表示在当前的2行3列的窗口的第4个位置上，添加1个子窗口。

 ![image-20201114115826220](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201114115826220.png)

ps：窗口是按行方向排序的，而且序号是从1，而不是0开始的。

### 13.4.2 imshow函数 ： 显示图像

```
matplotlib.pyplot.imshow(X,cmap=None)
```

- X : 图像信息，可以是各种形式的数值
- cmap：色彩空间。默认值为null，默认使用RGB（A）显示彩色图像。





# 第14章 傅里叶变换

![image-20201116112536225](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201116112536225.png)

**知识点把握：**

- **图像处理**：空间域处理 + 频率域处理
  - **空间域处理**：直接对图像内的像素进行处理。主要划分为 **灰度变换** + **空间滤波**。
    - **灰度变换**：对图像内的单个像素进行处理，比如调节对比度、处理阈值等。
    - **空间滤波**：设计图像质量的改变，例如图像平滑处理。
  - **频率域处理**：先将图像变换到频率域$\longrightarrow$ 在频率域对图像进行处理 $\longrightarrow$ 反变换将图像从频率域变换到频率域 。

**本章**：从    **理论基础**   、   **基本实现**   、   **具体实现**   等角度对傅里叶进行简单介绍。



## 14.1 理论基础

- 傅里叶级数：任何  **周期函数**  都可以表示为不同频率的  **正弦函数**  和的形式。
- 傅里叶变换：从  **频域的角度**  完整地表述   **时域信息**。傅里叶变换的结果表示：
  - **实数图像**（real image）+  **虚数图像**（complex image）
  - **幅度图像**（magnitude image）+  **相位图像** （phase image）
- 实例处理中，不同的频率函数间会存在  **时间差**，这个时间差，在频率中就是  **相位**。
- 频率中的图像：
  - **低频信息**：图像内变换缓慢的灰度分量。
  - **高频信息**：图像内变化越来越快的灰度分量，是由灰度的尖锐过度造成的。
- **傅里叶变换作用**：图像增强、图像去噪、边缘检测、特征提取、图像压缩和加密等。

## 14.2 Numpy实现傅里叶变换

Numpy模块中的   **fft2()函数**  可以实现图像的傅里叶变换。

### 14.2.1 实现傅里叶变换

- 1.  **numpy.fft.fft2() 将图像变换到频域。**

  ```
  返回值 = numpy.fft.fft2(原始图像)
  ```

  - **原始图像**：类型应是灰度图像。
  - **返回值**：复数数组（complex ndarray）
  - **brief** ：函数处理得到频谱信息，此时图像频谱中的零频率分量位于频谱图像的左上角。

- 2. **numpy.fft.fftshift() 将零频率成分移动到频域图像的中心位置。**

  ```
  返回值 = numpy.fft.fftshift(原始频谱)
  ```

- 3.  **为了显示图像，需要将它们的值调整到[0,255]的灰度空间内**

  ```
  像素新值 = 20*np.log(np.abs(频谱值))
  ```

  - 图像傅里叶变换后，得到一个复数数组。为了显示图像，需要将它们的值调整到[0,255]的灰度空间内。



### 14.2.2 实现逆傅里叶变换

在**傅里叶变换**过程中：使用了numpy.fft.fftshift()函数移动频率分量。

在**逆傅里叶变换**中：需要先使用numpy.fft.ifftshift() 函数将  **零频域分量**   移到原来的位置，再进行  **逆傅里叶变换**。

-  **numpy.fft.ifftshift()** 是 **numpy.fft.fftshift()**  的逆函数。

  ```
  **numpy.fft.调整后的频谱 = numpy.fft.ifftshift(原始频谱)
  ```

- **numpy.fft.ifft2() 实现逆傅里叶变换，返回空域复数数组。** 

  ```
  返回值 = numpy.fft.ifft2(频域数据)
  ```

  - numpy.fft.ifft2() 的返回值仍旧是一个复数数组。

- **将信息调整至[0,255]灰度空间内**。

  ```
  iimg = np.abs(逆傅里叶变换结果)
  ```




### 14.2.3 高通滤波示例

- 允许低频信号通过，低通滤波器。
- 允许高频信号通过，高通滤波器。

## 14.3 OpenCV实现傅里叶变换

OpenCV提供了函数  **cv2.dft()**  和  **ev2.idf()**  来实现傅里叶变换和逆傅里叶变换。

### 14.3.1 cv2.dft() : 实现傅里叶变换

1. 转为频域

```python
返回结果 = cv2.dft(原始图像，转换标识)
```

- 原始图像 ： 先用np.float32()将图像转换成np.float32()格式
- 转换标识 ： 通常为“ cv2.DFT_COMPLEX_OUTPUT”,用来输出一个复数阵列。

2. 返回结果需要用 numpy.fft.fftshift() 将   **零频率分量**   移到频谱中心。

```
dftShift = np.fft.fftshift(dft)
```

3. 频谱图像还是一个由实部和虚部构成的值。要将其显示出来，还要用 cv2.magnitude() 计算频谱信息的    **幅度**。

```
返回值=cv2.magnitude（参数 1，参数 2）
```

- 参数1：浮点型x坐标值，也就是  **实部**。
- 参数2∶ 浮点型y坐标值，也就是  **虚部**，它必须和参数1具有相同的大小（size 值的大小，不是 value 值的大小）。
- cv2.magnitude() 的返回值是参数1和参数2的平方和的平方根 。  I 为原始图像 。 

![image-20201118094041231](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201118094041231.png)

4. 将幅度值映射到灰度图像的灰度空间内[0,255] 。

   ```
   result = 20*np.1og（cv2.magnitude（实部，虚部））
   ```

   

### 14.3.2 cv2.idft() : 实现逆傅里叶变换

反过来啦。

### 14.3.2 低通滤波示例

做个掩模，与原图像进行与运算，滤掉高频。









# 第15章 模板匹配

![image-20201118094803011](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201118094803011.png)

**模板匹配**：用  **模板图像B**  在 输入  **图像A**  上滑动，遍历所有像素以完成匹配。



## 15.1 模板匹配基础

### 15.1.1 cv2.matchTemplate() ： 完成模板匹配

```
result = cv2.matchTemplate(image, temp1, method[, mask])
```

- image：原始图像。 必须为8位或者32位的浮点型图像。
- templ ：模板图像 。   尺寸必须小于或等于原始图像，并且与原始图像具有相同的类型。
- method ： 匹配方法。 有6种可能取值。

![image-20201118095530005](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201118095530005.png)

- result：由每个位置的比较结果所构成的一个结果集。类型是单通道的32位浮点数。
  - 原始： W*H
  - 模板： w*h
  - 返回值：（W-w+1）*（H-h+1）



### 15.1.2  不同的method，不同的result

- method = cv2.TM_SQDIFF / cv2.TM_SQDIFF_NORMED
  - result 为 0 表示匹配度最好，值越大，表示匹配度越差。
- method = cv2.TM_CCORR /  cv2.TM_CCORR_NORMED /  cv2.TM_CCOFF / cv2.TM_CCOFF_NORMED
  - result的值越大，表示匹配度越好。

确定method后，再确定查找   **result**  中的 **最大值**，还是查找  **最小值**。

查找  **最值**  与  **最值所在的位置** ，可以使用cv2.minMaxLoc() 来实现。

```python
minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(src, [,mask])
```

- src 为单通道数组。
- minVal为返回的最小值，如果没有最小值，则可以是 NULL（空值）。
- maxVal为返回的最大值，如果没有最小值，则可以是 NULL。
- minLoc 为最大值的位置，如果没有最大值，则可以是 NULL。
- maxLoc 为最大值的位置，如果没有最大值，则可以是 NULL。

## 15.2 多模板匹配

有时候，要搜索的模板可能在输入图像内出现了多次，这是需要找出多个匹配结果。

- cv2.minMaxLoc()仅仅能够找出最值，无法给出所有匹配区域的位置信息。
- 想匹配多个结果，需要利用阈值分割。



下面分步骤介绍如何获取多模板匹配的结果。

##### 1.获取匹配位置的集合

**np,where()**  可以找出在函数 cv2.matchTemplate() 的返回值中，哪些位置的值是大于阈值threshold 。

```
loc = np.where(res>=threshold) 
```

- res是函数 ev2.matchTemplate（）进行模板匹配后的返回值
-  threshold 是预设的阈值
- loc是满足"res >=treshold"的像素点的索引集合。

##### 2.循环

获取匹配值的索引集合后，采用如下语句遍历所有匹配的位置，对这些位置做标记：

```python
for i in 匹配位置集合：
	标记匹配位置。
```



##### 3.在循环中使用函数zip()

函数zip() 用可迭代的对象作为参数，将对象中对应的元素打包成一个个元素，然后返回由这些元组组成的列表。

如果希望循环遍历由mp.where（）返回的模板匹配索引集合：

```python
for i in zip(*模板匹配索引集合)：
	print(i)
```



##### 4.调整坐标

- 函数 numpy.where（）可以获取满足条件的模板匹配位置集合。

- 然后可以使用函数 cv2.rectangle（）在上述匹配位置绘制矩形来标注匹配位置。



##### 5.标记匹配图像的位置

 cv2.rectangle（）可以标记匹配图像的具体位置，分别指定要标记的原始图像、对角顶点、颜色、矩形边线宽度即可。

关于矩形的对角顶点∶

- 其中的一个对角顶点A可以通过for循环语句从确定的满足条件的 **"匹配位置集合"** 获取。

- 另外一个对角顶点，可以通过顶点A的位置与模板的宽（w）和高（h）进行运算得到。

  因此，标记各个匹配位置的语句为∶

  ```python
  for i in 匹配位置集合：
  	cv2.rectangle(输入图像, i, (i[0]+w, i[1]+h),255,2)
  ```

  

# 第16章 霍夫变换

![image-20201118110308972](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201118110308972.png)

**知识点把握**：

- **霍夫变换**：在图像中寻找直线、圆形以及其他简单形状的方法。
- **cv2.HoughLines()** : 在图像内寻找直线。
- **cv2.HoughCircles()** : 在图像内寻找圆。



## 16.1 霍夫变换原理

### 16.1.1 霍夫变换原理

与笛卡儿空间和霍夫空间的映射关系类似∶

- 极坐标系内的  **一个点**  映射为霍夫坐标系内的  **一条线**。
- 极坐标内的  **一条线**  映射为霍夫坐标系内的  **一个点**。



### 16.1.2 HoughLines函数

##### 16.1.2.1  cv2.HoughLines() :  霍夫直线变换

该函数要求所操作的源图像是一个二值图像。霍夫变换前先将源图像进行二值化，或者进行Canny边缘检测。

```python
lines  = cv2.HoughLines(image , rho, theta, threshold)
```

- image :  输入图像。 8位单通道二值图。
- rho ： 以像素为单位的距离r的精度。 一般情况下，使用的精度是1 。
- theta : 角度 $\theta$ 的精度。 一般为 $\pi/180 $ , 表示搜索所有可能的角度。
- threshold : 阈值。 该值越小，判定出的直线就越多。

cv2.HoughLines() 检测的是图像中的  **直线**  而不是  **线段**。因此检测到的直线是没有端点的。

所以Hough变换所绘制的  **直线**  的都是穿过整副图像的。



**绘制直线方法**： 

- 对于垂直方向的线： 计算它与图像水平边界的交叉点，然后在两个交叉点之间画线。
- 水平方向的线： 也类似。
- 绘线时使用的函数： cv2.line()  。   
- cv2.line()方便之处： 即使点的坐标超出了图像的范围，也能正确地画出线来。 因此，没有必要检查交叉点是否位于图像内部。
- 遍历函数 cv2.HoughLines() 的返回值lines，就可以绘制出所有的直线。

![image-20201119103316349](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119103316349.png)

**霍夫变换缺点**： 可能将图像中有限个点碰巧对齐的非直线关系检测为直线。 复杂背景的图像，误检尤为明显。

**解决：** 提出霍夫变换的改进版----概率霍夫变换。



### 16.1.3 HoughLinesP函数 ： 概率霍夫变换

**概率霍夫变换**： 没有考虑所有的点。只需要一个足以进行线检测的随机点子集。改进点：

- 所接受直线的最小长度。
- 接受直线时允许的最大像素点间距。

```python
lines = cv2.HoughLinesP(image , rho, theta, threshold, minLineLength, maxLineGap)
```

- threshold : 阈值。该值越小，判定出的直线越多。值越大，判定出的直线就越少。
-  minLineLength ： 接受直线的最小长度。默认为0
- maxLineGap：控制接受共线线段之间的最小间隔。
- lines ： 由numpy.ndarray类型的元素构成。其中每个元素都是一对浮点数，表示检测到的直线的参数， 即 $(r,\theta)$

![image-20201119104919599](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119104919599.png)

## 16.2  cv2.HoughCircles() 霍夫圆环变换

只要是能够用一个参数方程表示的对象，霍夫变换都能做检测。

**检测图像中的圆**：

- 第一轮筛选找出可能存在圆的位置（圆心）
- 第二轮根据第一轮的结果筛选出半径大小。

```python
circles = cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
```

- method : 代表的是霍夫圆检测中两轮检测所使用的方法 。 
- dp∶累计器分辨率，它是一个分割比率，用来指定图像分辨率与圆心累加器分辨率的比例。
- minDist∶ 圆心间的最小间距。
- param1∶该参数是缺省的，在缺省时默认值为 100。它对应的是Canny 边缘检测器的高阈值（低阈值是高阈值的二分之一）。

- param2∶圆心位置必须收到的投票数。只有在第1轮筛选过程中，投票数超过该值的圆，才有资格进入第2轮的筛选。因此，该值越大，检测到的圆越少;该值越小，检测到的圆越多。缺省。

- minRadius∶ 圆半径的最小值，小于该值的圆不会被检测出来

- maxRadius∶ 圆半径的最大值，大于该值的圆不会被检测出来。
- circles∶ 返回值，由圆心坐标和半径构成的 numpy.ndrray。

![image-20201119110754353](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119110754353.png)







# 第17章  图像分割与提取

![image-20201119111013591](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119111013591.png)

**知识点把握**：

- 我们在看监控视频时，对固定背景下的视频内容毫无兴趣，感兴趣的是视频中的妹仔。怎么提出出妹仔呢？

- 前面学了 图像形态学变换、阈值算法、图像金字塔、图像轮廓、边缘检测等方法对图像进行分割。
- 本章介绍使用分水岭算法及GrabCut算法对图像进行分割与提取。



## 17.1 用分水岭算法实现图像分割与提取

分水岭算法将图像形象地比喻成地理学上的地形表面，实现图像分割。

### 17.1.1 算法原理

- 任何一副灰度图像，都可看作地形。灰度值高区域为   **山峰**，灰度值低区域为  **山谷**。
- 往山谷中注水，防止不同山谷间的水交汇，需要在水流可能汇合处  **构建堤坝**。
- 该过程将图像分成两个不同的集合： **集水盆地** 和  **分水岭线** （堤坝）
- 堤坝也就是对原始图像的分割。

由于噪声的影响，上述基础分水岭算法经常会得到过度分割的结果。

为了改善图像分割效果，人们提出了基于掩模的改进的分水岭算法。

### 17.1.2 cv2.watersheld() 实现分水岭

具体实现过程中，还需要借助于形态学函数、距离变换函数、cv2.distanceTransform()、 cv2.connectComponents() 来完成图像分割。

##### 17.1.2.1 形态学函数回顾

- 开运算去除前景外的噪声：先腐蚀、再膨胀
- 原始图像 - 腐蚀图像  =  图像边缘
- **形态学获取边界缺点**： 仅适用于比较简单的图像，如果前景对象存在连接的情况，形态学操作就无法精确获取各个字图像的边界了。



##### 17.1.2.2 距离变换函数 distanceTransform

- 图像内的各个子图有连接时，借助于距离变换函数 cv2.distanceTransform()  可以方便地将前景对象提取出来。
- **cv2.distanceTransform() 计算结果**： 反映了各个像素与背景（值为0的像素点）的距离关系。
  - 前景对象的   **中心（质心）**   距离值为0的像素点距离较远： 得到**较大**的值。
  - 前景对象的  **边缘**   距离值为0的像素点较近： 得到一个**较小**的值。
- 对上述计算结果阈值化，就可以得到图像内子图的中心、骨架等信息。
- 距离变换函数cv2.distanceTransform()  可以用于计算对象的中心，还能细化轮廓、提取图像前景等。

```python
dst = cv2.distanceTransform(src, distanceType, maskSize[, dstType])
```

- src : 8位单通道的二值图像。
- distanceType为距离类型参数：

![image-20201119115515650](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119115515650.png)

![image-20201119115528281](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119115528281.png)



- maskSize 为掩模的尺寸 。当 distanceType=cv2.DISTL1或 cv2.DIST_C时，maskSize强制为3（因为设置为3和设置为5及更大

  值没有什么区别）。

  ![image-20201119115639055](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201119115639055.png)

  

  

##### 17.1.2.3  确定未知区域

- cv2.distanceTransform() 获得   **前景图像 F**，确定了   **背景图像 B** 
- 剩下的就是  **未知区域UN** ， 这部分区域正是分水岭算法要进一步明确的区域。
- ​    **未知区域UN** =  （**图像O**  -   **背景图像 B** ） -  **前景图像 F**
-   **图像O**  -   **背景图像 B**  可以通过对图像进行形态学的膨胀操作得到。

### 17.1.3 分水岭算法图像分割实例

## 17.2 交互式前景提取