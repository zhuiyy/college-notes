# 写在前面
2025 春季

考试真挺难的, 这篇笔记不够用, 幸好考试占分不多.

# 1.课程介绍
# 2.python pytorch 数学基础
## 回归
### 过拟合的解决方案
1) 增大训练数据量
2) 减小模型复杂度
3) 正则化(调先验)
4) 早停法
## 概率论
### 贝叶斯定理
$$P(Y|X)=\frac{P(X|Y)P(Y)}{P(X)}=\frac{P(X|Y)P(Y)}{\sum_{Y}P(X|Y)P(Y)}∝{P(X|Y)P(Y)}$$
其中
$$P(Y)$$
是先验概率(prior), 表示Y在X作用前估计的概率分布.
$$P(X|Y)$$
是似然函数(likelihood), 表示假设Y的情况下, 我们观测到数据X的概率.
$$P(Y|X)$$
是后验概率(posterior), 表示Y在X作用后的概率分布.

我们只能调整X, 希望最后的P(Y|X)最大, 所以可以通过最大化likelihood * prior来得到
### 概率密度函数PDF与累积分布函数CDF
### 数学期望
### 方差Var
$$Var = E(X^2)-E(X)^2$$
### 协方差Cov
$$Cov(X,Y)=E_{X, Y}[(X-E(X))(Y-E(Y))] = E(XY)-E(X)E(Y)$$

| 协方差符号 | 含义                          | 关系图示              |
|------------|-------------------------------|-----------------------|
| **正值**   | 两变量倾向于同向变化          |  ↗️ X增大 → Y增大       |
| **负值**   | 两变量倾向于反向变化          |  ↘️ X增大 → Y减小       |
| **零**     | 两变量无线性关系（可能非线性） | 数据点无规律分布       |
### 概率分布(PDF)
1) 均匀分布
2) 高斯分布(正态分布)
3) 拉普拉斯分布
### 概率学派
1) 频率学派
    
    最大似然估计: 调整参数最大化测试数据出现的概率
2) 贝叶斯学派:
    
    最大后验概率: 认为参数本身就有一个先验的分布概率, 在考虑这个的条件下最大化测试数据出现的条件概率.
## 信息论
交叉熵损失

# 3.机器学习基本情况
##  机器学习的基本任务分类
1) 有监督学习(分类问题, 回归问题)
2) 无监督学习(k_近邻分类器, 聚类问题, 密度估计, 降维)
3) 半监督学习
4) 弱监督学习
5) 强化学习
## 机器学习的表现评估
loss

# 4.线性回归与逻辑回归
线性模型通过学习特征的特定线性组合系数, 达到预测的目的. 

### 线性回归
#### 模型
给定数据:
$$\{(X_{i}, y_{i})\}_{i=1}^{m} \subseteq R^{n} \times R$$
我们的目标是找到一个线性函数:
$$f(X)=W^{T}X + b$$
其中
$$W \in R^{n}, b \in R$$
使得预测值:
$$\hat{y} = f(X) = W^{T}X + b$$
接近真实发生X的情况下, y的值.
#### 估计损失的方法
均方误差方法:
$$Loss = E(f(X) - y)^{2}$$
#### 最小二乘法

存在f使得Loss = 0等价于线性方程组:

$$W^{T}X_{i} = y_{i} - b$$

有解. 为了方便计算, 我们一般会吧b吸纳进X与W中, 在每个X数据末尾加上一个1, 这样可以把b也看作是X的一部分, W同时组合X与1, 可以同时训练.
于是$A$ 的行向量为 $[X_{i}^{T}, 1]$ , $Y$ = $[y_{i}]_{i=1}^{m} \in R^{m}$.


我们对Loss求偏导得到最佳结果需要满足的正规方程:

$$A^{T}A\hat{W} = A^{T}Y$$

其中$\hat{W}$ 是使得Loss最小的$W$.

分析$A^{T}A$:

$$n+1级方阵$$
$$Rank(A^{T}A) = Rank(A)$$

1) $A^{T}A$可逆, 则有唯一解$W = (A^{T}A)^{-1}A^{T}Y$
2) $A^{T}A$不可逆, 则有多个解, 我们选择使得Loss最小的解.

由上分析知$A^{T}A$可逆等价于$A$列满秩, 样本数量(m)小于特征维度+1(n+1)时必定不可逆(A行数小于n+1).

不可逆的时候, 可以通过向Loss中增加正则损失项来缓解.

比如L2正则, 添加完Loss梯度=0的方程变成:
$$(A^{T}A - \lambda I)\hat{W} = A^{T}Y$$

使得可逆.

#### 正则化
1) L1正则: 相当于先验估计参数符合拉普拉斯分布, 使用L1正则可以使得不少无用参数归零, 可以用于特征选择.

2) L2正则: 相当于先验估计参数符合高斯分布, 使用L2正则可以使得参数绝对值大大降低, 防止过拟合.

#### 梯度下降法
即使可逆, 求解逆矩阵也十分麻烦, 不如使用梯度下降法作为搜索问题处理.

我们对Loss求梯度, 并反方向变化参数, 使得Loss快速减小.

##### 学习率大小问题
### 逻辑回归

    注意!!!逻辑回归是一种分类问题!!!!

逻辑回归的任务是接受数据X, 并输出一个[0, 1]间实数, 代表预测为正类的概率.

#### 模型
具体模型就是线性回归 + sigmoid

#### Loss
选用交叉熵, 对于分类问题, 交叉熵的梯度更陡, 更容易收敛.

同时, 交叉熵符合MLE思想

#### 局限性
由于本质线性, 无法解决异或分类问题.

我们需要更多层次的模型.

# 5.神经网络基础
## 激活函数的选择
relu: 防止梯度消失(但引入神经元失活)
## dropout
测试或者应用过程中, 停止dropout, 增强泛化能力.

# 6.卷积神经网络基础
## 卷积层
### 卷积层参数

$H_{in} * W_{in}$: 原数据大小

padding: 源数据外围填充, 使得卷积后输出大小不至于过小.

stride: 步长, 卷积核滑动的步长(有两个方向).

kernel_size: 卷积核大小.

有
$$H_{out} = \frac{H_{in} + 2*padding - kernel\_size}{stride} + 1$$

$$W_{out} = \frac{W_{in} + 2*padding - kernel\_size}{stride} + 1$$

但这仅仅是**1**个2d图片经过**1**个卷积核后得到的结果.

如果我们严格定义一个卷积核组的参数:

| 变量名称 (中文) | 变量名称 (英文) | 维度/形状描述 | 说明 |
| :--- | :--- | :--- | :--- |
| 输入尺寸 | Input size | `(height, width, channels)` | 通常为图像或上一层的输出特征图的尺寸。 |
| 卷积核高度 | filter_height | `int` | 卷积核的空间高度。 |
| 卷积核宽度 | filter_width | `int` | 卷积核的空间宽度。 |
| 输入通道数 | input_channels | `int` | 卷积核将处理的输入特征图的通道数。对于RGB图像，为3。在CNN中，它必须与前一层的输出通道数（即前一层的n_filters）匹配。 |
| 滤波器数量 | n_filters | `int` | 该卷积层中使用的独立滤波器的数量。每个滤波器会生成一个输出通道。这直接决定了当前层的输出通道数。 |
| 滤波器形状 | Filter shape | `(filter_height, filter_width, input_channels, n_filters)` | 定义了卷积核的完整形状。在某些框架中可能是 `(n_filters, input_channels, filter_height, filter_width)`。 |
| 填充量 | padding | `int` 或 `(pad_h, pad_w)` 或 `string` | 在输入特征图的边界周围添加的像素数量。常见的有 `"valid"` (不填充), `"same"` (填充以使输出空间维度与输入相关), 或具体的像素值如 1x1 (P=1)。 |
| 步长 | Strides | `int` 或 `(stride_h, stride_w)` | 卷积核在输入特征图上滑动时的步长。1x1 表示每次移动1像素，2x2 表示每次移动2像素。 |
| 输出高度 | output_height | `int` | 卷积层输出特征图的高度。 |
| 输出宽度 | output_width | `int` | 卷积层输出特征图的宽度。 |
| 输出通道数 | output_channels | `int` | 卷积层输出特征图的通道数，等于 n_filters。 |
| 输出形状 | Output shape | `(output_height, output_width, output_channels)` | 卷积层输出的完整特征图形状。 |
| 输出尺寸计算公式 | Output dimension formula | `O = ⌊(I + 2P - F) / S⌋ + 1` | 用于计算输出特征图的空间维度（高度或宽度）。其中 `I` 为输入维度，`F` 为滤波器维度，`P` 为填充量，`S` 为步长。`⌊⋅⌋` 表示向下取整。 |

#### 感受野
某一个神经元的原始输入范围, 一般等于filter_height * filter_width.

## 池化层
max pooling, mean pooling等.

可以看作一个stride = filter_size的卷积层.

池化层的作用是降低参数量, 减少计算量, 提升模型的表达能力.
### 空间金字塔池化
不同大小的池化结果全连接

## 反卷积算法
插入空值(空洞卷积)
## 网络架构发展
Alex Net : 创造历史

VGG16 : 轻量化网络

ResNet : 残差网络, 跨层连接, 解决梯度消失问题

squeeze/mobile/shuffle net : 更多样的轻量化网络

# 7.卷积神经网络的应用
## 目标检测(回归)
### 数据集
Pascal VOC, MS COCO

### 效果评估方式
交并比(IoU), 平均精度(mAP)

其中AP:

    精度率 : Precision = TP / (TP + FP) (实际为正占预测为正的比例)
    召回率 : Recall = TP / (TP + FN) (预测为正占实际为正的比例)
    真阳性 : True Positive (TP)
    假阳性 : False Positive (FP)
    真阴性 : True Negative (TN)
    假阴性 : False Negative (FN)

### 目标检测算法
#### RCNN
1) 选择性搜索Selective Search提取候选区域
2) 候选区域调整为固定大小
3) 输入卷积神经网络(如VGG)提取特征
4) 特征进入分类器(如支持向量机SVM)
5) 回归获取目标框位置
6) 非极大值抑制(NMS): 可以保留同一个目标所有可选框中最好的
##### 缺陷
1) 选择性搜索慢
2) 候选区域尺寸变化导致宽高比例变化, 分类不准
3) 每个结果单独进卷积网络, 慢
4) 非端到端
#### SPPNet
1) 把整个图片塞进特征提取器
2) 选择性搜索找**在特征图内**找候选区域
3) 备选特征图通过金字塔池化得到统一长度的全连接向量
4) 用分类器分类
5) 回归得到目标框
6) 非极大值抑制
##### 缺陷
1) 选择性搜索慢
2) 非端到端
#### Fast R-CNN
1) 把整个图片塞进特征提取器
2) 选择性搜索找**在候选区域内**找特征图
3) 对备选特征图进行感兴趣区域池化操作(ROI)
4) 用神经网络同时进行特征提取和分类
5) 回归得到目标框
6) 非极大值抑制
##### 缺陷
1) 选择性搜索慢
2) 伪端到端
#### Faster R-CNN
1) 把整个图片塞进特征提取器
2) 使用区域提议网络(Region Proposal)生成高质量候选区域
3) 对备选特征图进行感兴趣区域池化操作
4) 用神经网络同时进行特征提取和分类
5) 回归得到目标框
6) 非极大值抑制
#### YOLO
1) 直接同时分类 + 预测框(以网格单元为单位)
2) 非极大值抑制
#### YOLOv2
1) 先验不同形状大小的预选框(提高分辨率, 准确性)
2) 同时分类 + 预测框
3) 非极大值抑制
#### SSD
1) 整个图片进行不同尺度的卷积, 获得不同尺度的特征图
2) 每个图上先验不同形状大小的预选框
3) 利用预选框预测
4) 非极大值抑制
## 图像分割(分类)
给每个颗粒(像素)分类

    语义分割是图像分割的子类, 当任务是把像素按照不同物体类别分类时, 就算是语义分割.

    实例分割也是图像分割的子类, 不仅要求语义分割, 还要求区分同一物体类别中的不同个体, 相当于还要做一个目标检测.

### 效果评估方式
像素级的交叉熵效果不好, 会偏向于面积大的物体.

Dice系数:
$$Dice = \frac{2|A\cap B|}{|A|+|B|}$$
### 图像分割算法
#### FCN(全卷积网络)
1) 下采样(encoder): 通过不断卷积和池化, 获得尺寸更小的特征图, 同时通过skip connection连接到decoder
2) 1x1卷积(1x1 conv): 降维, 获得通道数个小图
3) 上采样(decoder): 通过反卷积, 逐渐恢复图像尺寸, 同时接收skip connection的输出获取更多信息
4) 按照像素softmax输出分类结果
#### SegNet
与FCN的区别比较微妙, 结构上与FCN类似.
#### PSPNet
1) 通过卷积神经网络提取特征
2) 通过金字塔池化全连接
3) 上采样
4) 经过一个卷积层, 得到预测
### 实例分割算法
#### Mask R-CNN
1) ResNet等提取特征
2) 特征图进行Region Proposal生成候选区域
3) ROI Pooling, 并对齐大小
4) 分类 + 位置回归(NMS)
5) 对每个分类后的框再进行语义分割, 完成实例分割

### 图像分割TRICKS
1) 数据增强: 边缘镜面反射
2) 损失加权: 增大边缘, 小面积物体的权重

## 人脸识别(分类)
检测人脸位置 + 将人脸对齐到图片中心 + 人脸身份识别.
### 数据集
MS1M
### 两个子任务
1) 人脸识别(Identification): 给定一个人脸数据库, 以及一个人脸图片, 判断属于哪个人.

2) 人脸认证(Verification): 给定两张人脸图片, 判断是否同属一个人. 
### 两种数据情况
1) Openset: 可能没有测试人的人脸信息
2) Closedset: 一定有测试人的人脸信息.
### 四种任务:
1) O-I: 通过卷积神经网络提取特征向量, 并与数据库比较, 如果有相似则输出类别, 否则输出Unknown.

2) O-V: 通过卷积神经网络提取特征向量, 如果两个向量相似度高则输出通过, 否则不通过.

3) C-I: 类似MNIST简单分类问题.
4) C-V: 做两次C-I, 看是否同属一类.
### 人脸识别算法
#### MobileFaceNet = ArcFace + MobileNetV2
##### 优势:
轻量级

## 姿态估计()
估计人的姿态, 需要确定关节, 以及那些关节应该相连.
### 两种思想
1) 自顶向下: 先通过目标检测把每个个体区分开, 再计算姿态信息.

    优势在于准确率高(如果目标检测得好)

    缺点是依赖目标检测, 而且推理时间与人数有关

2) 自底向上: 先计算关节等关键位置, 再把这些位置分配给不同人.

    优势在于不需要目标检测, 推理时间固定

    但是难以将关键位置分配给不同的人

### 姿态估计算法
#### CPM(单人估计)
1) 目标检测找人
2) 多次利用之前的输出计算关键点, 不断精细化, 这个过程中可能会把误估计的改正过来.
##### 优势
感受野大, 准确率高
#### OpenPose(多人估计)
CPM + 自底向上

#### PPN(多人估计)
YOLO(自顶向下) + OpenPose
## 其他应用
人员重识别, 人物属性分类, 深度估计, 风格迁移, 超分辨率, 图像翻译, 语义生成图像.
# 8.GAN初步
判别式模型注重找决策边界, 即条件概率分布

而生成式模型注重生成, 找联合概率分布.
## 朴素GAN
### Loss 最大最小博弈
$$Loss = min_{G}max_{D}E_{x\sim p_{data}(x)}[logD(x)] + E_{z\sim p_{z}(z)}[log(1-D(G(z)))]$$

希望在D判别能力最强的条件下, G的能骗过D.

### 训练过程
1) 采样一批噪声与真样本
2) G利用噪声生成假样本
3) 假样本和真样本都喂给D, D计算判别损失并学习
4) G计算生成损失并学习
5) 重复1-4

    
如果一上来就把D训练至最佳, 就会导致模式崩溃(趋向于生成某几种运气很好能骗过D的图片)/梯度消失(给回的梯度全是0), G无法学习.

### 结束状态:
D给出的结果趋近于0.5(对于所有输入无法判断真伪)

G和D的loss应该在一个小范围内波动, 不应增高或降低至0, 否则没有对抗的效果.
## DCGAN
加入卷积神经网络用于生成, 质量高
## lossfunction比较: GAN与VAE(使用mse)
![compare](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/gan%E4%B8%8Evae.png)

MSE会忽略面积比较小的细节.

# 9.GAN算法选讲
## 有条件的GAN
### Conditional GAN(cGAN)
在朴素GAN基础上, 向G添加类别信息, 并让D预测类别.

如果类别信息更复杂(作为一个句子), 则需要一个encoder解析句子特征解决语言问题, 同时, 需要多种不同输入: (真句子, 匹配的真实图片), (真句子, 不匹配的真实图片), (真句子, 生成的图片), 只有第一种应该被判为真.


## 寻找潜在表示
### 暴力优化一
拿一个已经训练好的G, 给定一张真实图片, G不学习, G的输入噪声按照G的输出与真实图片的差距进行学习, 最终找到潜在表示.

#### 缺陷
太慢
### 暴力优化二
以image to image为例.

给定一个已经训练好的条件GAN, G不变, 把D替换为一个编码器E, 输入图片, 输出潜在表示(噪声). 训练时, 把一个噪声与label喂给G, 得到图片链接label, 喂给E, 得到潜在表示与, 用MSE评价潜在表示与噪声差距, 并训练E.

对于image to image, 应用时, 把真实图片+label输入E, 得到潜在表示, 然后把潜在表示与目标label输入G, 得到目标域图片.
#### 缺陷
E训练时没见过真图, 导致模式塌陷(倾向于生成某几类特定图片).
### 公共编码法
以AI换脸为例.

a的脸, 输入编码器, 得到潜在表示a, 输入A解码器, 得到a的近似图; 再输入b的脸, 输入同一个编码器, 得到潜在表示b, 输入B解码器, 得到b的近似图, 比较并学习.

使用时, 输入a的脸, 通过解码器得到潜在表示a, 再输入**B的编码器**得到图片, 图中a的脸被换为b的.

### BiGAN
给(噪声, 图片)对, 把噪声输入G, 得到生成图; 把原始图片输入E, 得到潜在表示.

把(噪声, 生成图), (潜在表示, 原始图)都输入D, 判断是否真实.

训练后E趋向于G的逆
## 无监督寻找潜在表示
### CoGAN
![cogan](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/Co.png)
可以同时生成两个域内有相关性的图片.
#### 缺陷
无法给定一个域的图片, 生成另一个域的对应图片.
### CycleGAN
#### 引
其实可以通过更改BiGAN, 把E和G改为两个E+G, 一个专注于domain AtoB, 一个专注于BtoA, 然后把图片对输给D

然而普通的对抗loss不够, 需要改进

#### 原理
![cyc](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/cyc.png)
注意上下两行是同两个E+G

还可以加入Identity loss, 直接给一个A图, 进入BtoA, 得到一个假A图, 计算MSE, 可以用于保留细节信息.
# 10.循环神经网络
用于处理时序数据
## word expression
### 1-hot
按位置编码, 维度爆炸, 词间无关系
### 词袋 bag of words
用单词频率表示句子, 维度继续爆炸, 词间无关, 丢失位置关系
### word embedding
用高维向量描述每一个词
#### 习得词嵌入
这是一种无监督算法, 通过词语的上下文位置关系, 判断词是否类似
### word2vec
用以下两种机制学习词嵌入
#### CBOW连续词袋模型
一个滑动窗口, 用两边的词预测中间的词概率.
#### SG
与CBOW相反, 用中间的预测两边, 词库中每个词出现的概率
#### 噪声对比估计NCE/负采样
这个估计方法比交叉熵好, 因为词库太大了, 尤其是负采样, 只用在词库中取几个负样本(错误/随机搭配的词组)即可计算loss
## 序列数据
可以按照时间步分成一系列数据
## 朴素循环神经网络
基本思想为, 将上一个时间步的某层结果(h)传给下一个时间步同步训练

我们一般会使用一个tanh作为激活函数

![va](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/va.png)

    (对于不同的任务, 有多种网络架构: 一对一, 一对多(图片描述), 多对一(句子情感分类), 异步多对多(对话机器人), 同步多对多(气象预测, 交通计数, 文本生成(每个时间步的输出词会变成下一个时间步的输入)))

### 缺陷
长期信息难以维持(权重一点一点变小)

## LSTM长短期记忆网络
精细化操作记忆, 可以存储长期, 短期记忆, 并且有记忆主动删除功能.
### 遗忘门(由上一步h和当前输入决定)
![f](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/forget.png)

ft中0代表完全忘记, 1代表完全保留.
### 输入门
![i](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/input.png)

C用于长期保留记忆(先遗忘, 再新增).

同时利用上一步h与当前步x决定记忆什么, 记忆多少.
### 输出门
![o](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/output.png)

输出门决定长期记忆(更新后)中哪些部分应该变成短期记忆(同时也是当前步的输出)用于下一时间步.

### 激活函数
用sigmoid而不用relu, 更符合遗忘, 记忆的功能

用tanh而不是sigmoid, 因为可以保留负值, 更准确, 多样, 也比sigmoid梯度大, 好算.

# 11.Attention and Transformer
## 动机
仍然存在长度依赖问题, lstm太耗力.
## self-attention 自注意力机制
### 全新词嵌入 QKV空间
Q 代表这个词需要的注意类别(如一个名词需要形容词注意, 一个形容词需要副词注意)
K 代表这个词可以注意到的类别(如一个形容词可以注意到名词)
V 代表这个词的

比如'creature'的Q向量正好会和'cute'的K向量很好的对应, 这表现为二者点积很大.

我们把所有词的Q和所有词的K挨个点积, 即矩阵乘法:

$$K^{T}Q$$

其中, (i, j)元代表j这个词的注意需求与i注意能力的对应, (i, j)元很大, 则认为i"注意到"j.

我们称

$$N = K^{T}Q$$

我们把这个矩阵做个softmax, 再与每个词的V向量(语义)相乘, 作为偏移量:

$$Z = softmax(\frac{K^{T}Q}{c})V$$

    注: c为缩放因子, 可以确保softmax梯度不过小, 一般取sqrt(Q向量的维度)

把Z与原始语义矩阵(并非V)相加, 就可以得到注意力后的语义矩阵.

如'creature'的语义可能在自注意力后变得更加接近'cute creature'.
### 其他自注意力机制
类似, 可能Q与K的对应方式不同, 比如线性组合.
## 多头注意力
映射到多组空间, 即有多组对应的QKV, 这些映射方法**独立**训练, 最后拼接输出.

### 注意力缺陷
没有位置信息
## Transformer
![trans](https://github.com/zhuiyy/zhuiyy/blob/main/picture%20bands/trans.png)

一个编码器, 一个解码器, 很多重复单元, 单元内层之间有残差连接.

1) 进行词嵌入与位置信息嵌入(句子向量= 词向量 + 位置编码)

        位置信息可以使用sin/cos编码方式
2) attention
3) 残差连接, 加和, 层规范化(均值为0, 方差为1)
4) 经过一个前馈网络(两层全连接, 中间是relu)
5) do 3.
5) 2.~5.重复n次
6) encoder结果不是直接输入decoder, 而是作为中间数据输入, decoder接受的是已经输出的目标序列, 用于预测下一个词
7) 连入掩蔽attention, 屏蔽未来序列信息.(使得注意力矩阵只有对角线以上的半部分(softmax前, 下半部分变成-inf))
8) do 3.
9) 一个多头attention, 引入encoder输出
10) do 3.~5.
11) 8.~11. m次
12) 全连接层, 输出概率
## 预训练过程
无标签预训练, 然后fine-tune
### GPT(decoder-only)
单项预测文本(只依赖左边文本信息), 多个transformer.
#### 预训练
1) 上文预测下一个词
2) 微调, 添加head层, 用于解决特定任务
### BERT
双向上下文, 预测中间缺失内容.
#### 预训练
1) 完形填空
2) 判断两个样本是否是上下文关系

# 大班课: 大语言模型
论断: 如果人类的思维一定能用语言呈现, 那么LLM可以模拟人类所有思维过程.

- pre-training 学会语言
- post-trainning 应用语言(微调, 对齐)
## GPT-3(decoder-only)
    encoding-embedding-(attention*96-add&norm-feedforward-add&norm-linear)*96-softmax

训练成本太高, 在成功之前会有无数次失败训练.

## Deepseek V1-3
### 技术细节
#### MOE混合专家模型
专家是每层多个相同架构的网络, 独立进行计算学习, 同时输出亲和度, 用于决定结果被发送给下一层的哪些专家.

    deepseek中, 采用共享+路由专家模型, 即有一些专家是固定启用的, 余下的通过亲和度选择.

训练过程中如果哪个Expert用的太多，
就通过概率、loss等方法惩罚这个Expert不要用太多.

MOE一般替换transformer中的前馈层.
#### MLA重复计算优化方案
比如预测'我来自北京'
1) 用'我', '来', '自', 预测'北':

        self attention中, 当前步的Q(北) 需要与K(我), K(来), K(自)计算, 把K都缓存下来.
2) 用'我', '来', '自', '北', 预测'京':

        不用再计算K(我), K(来), K(自).

但是这样, 所需空间极大.

MLA可以利用神经网络把矩阵进行低秩压缩, 以及解压缩. 
#### MTP多token预测
训练时, 每次预测三个token而不是一个; 推理时, 可以传统地每次预测一个, 或者投机加速, 预测多个.
## Deepseek R1
在Deepseek V1-3的基础上, 加入了强化学习, 使得模型可以自主学习, 而不是依赖人工.
### 技术细节
首个仅通过RL激发LLM推理能力的开源项目, 证明大模型的推理能力可以蒸馏到小模型.

V3经过Pure RL得到DeepSeek-R1-Zero.

随着测试时间计算的增加，模型自发地展
现出复杂的行为, 例如:
- 反思（模型重新审视和评估其先前的步骤）
- 探索问题解决的替代方法

## 新技术TTS
指LLM推理时动态调配算力的策略:

- 垂直扩展: 通过量化、算子优化加速单请求.

- 水平扩展: 用并行计算和批处理提升吞吐, 实现低延迟、高并发与低成本的最优平衡.



## LLM评估
- Humanity's Last Exam
- LiveCodeBench
- SWE bench

# 12. 用搜索解决问题

    以下为数算笔记内容
## 问题建模
1) 初始状态$S_{0}$
2) 可选动作
3) 状态转移模型(graph)
4) 目标状态$S_{next}$
5) $cost$

| **算法**                | **核心思想**                                                                 | **优点**                          | **缺点**                          | **适用场景**                      |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **广度优先搜索 (BFS)**  | 逐层扩展，使用队列。                                                        | 完备、最优（单步成本一致）        | 高内存（O(b^d)）                  | 最短路径问题（如迷宫、罗马尼亚地图） |
| **深度优先搜索 (DFS)**  | 深入分支优先，使用栈。                                                      | 低内存（O(d)）                    | 不完备（可能无限循环）、非最优    | 内存受限、无需最优解（如部分解探索） |
| **一致代价搜索 (UCS)**  | 按路径成本 `g(n)` 优先扩展，使用优先队列。                                   | 最优（单步成本任意）              | 时间效率低（O(b^{1+C*/ε})）       | 成本敏感的最优路径（如交通规划）     |
| **贪婪最佳优先搜索**    | 依赖启发式 `h(n)` 选择节点，优先接近目标。                                   | 速度快（启发式好时）              | 不保证最优解                      | 快速近似解（如实时游戏AI）          |
| **A*搜索**              | 综合 `g(n)`（实际成本）与 `h(n)`（启发式），`f(n)=g(n)+h(n)`，优先队列扩展。 | 完备、最优（h可采纳或一致）       | 需设计高质量 `h(n)`               | 最优路径规划（如机器人导航）        |
| **迭代加深搜索 (IDS)**  | 逐层增加深度限制，重复执行深度受限的DFS。                                    | 低内存、完备、最优（单步成本一致）| 时间冗余（重复扩展浅层节点）      | 内存受限的最优解问题（如八数码）    |
| **双向搜索**            | 同时从起点和终点展开搜索，中间相遇。                                         | 时间空间减半（O(b^{d/2})）        | 需已知目标状态、实现复杂          | 已知目标的双向路径问题（如社交网络） |


不同搜索算法的本质区别在于图的展开方法。
## openlist & closedlist

对于一个搜索过程的某一时刻，openlist代表马上将要搜索的一部分节点，closedlist代表已经搜索过的节点。

对于openlist与closedlist的处理产生多种搜索算法

## 图搜索与树搜索

1) 图搜索：同时维护openlist与closedlist，closedlist中节点不会被重复搜索(原则上)，大大提高搜索效率，但需要大量空间占用。

2) 树搜索：只维护openlist，每个节点有可能被搜索多次，甚至导致无限循环，但好处是不需要额外空间维护closedlist.

## 基本搜索算法
### BFS-广度优先搜索
BFS强调搜索的广泛度，使用一个队列维护openlist.队列是先进先出的。

如状态t时，openlist为\[1,4,6\](数字代表节点)，于是会先处理队首元素1，若1是目标节点，则搜索结束；否则，将1的子节点2,3加入队列，此时openlist变为\[4,6,2,3\]，继续处理队首元素4，以此类推。

BFS完备且最优(如果相邻节点距离为定值)，但需要大量空间，时间复杂度为O(b^d)，其中b为分支因子，d为搜索深度。

图搜索与树搜索都可以应用BFS

### DFS-深度优先搜索
DFS强调搜索的深度，使用一个栈维护openlist.栈是先进后出的。

如状态t时，openlist为\[1,4,6\]，先处理栈顶元素1，若1是目标节点，则搜索结束；否则，将1的子节点2,3加入栈，此时openlist变为\[2,3,6,4\]，继续处理栈顶元素2，以此类推。

DFS不完备(可能循环, 除非维护closed list)，不最优(除非完全遍历，这时也不必再说什么深度优先了)

### 深度受限搜索
在DFS的基础上，要求搜索深度不超过常数L

如此可知，深度受限搜索不完备(可能根本搜不到)，不最优(除非完全遍历深度L以内的图，这时也不必再说什么深度优先了)

### 迭代加深搜索(BFS用DFS实现)
做多轮DFS，令L由0递增，直到找到目标。

虽然每次DFS会重复搜距离近的节点，但空间复杂度比BFS低得多。

迭代加深搜索是完备的，最优的。

### UCS-一致代价搜索(Dijkstra)
UCS强调搜索的路径成本，使用一个优先队列维护openlist.优先队列是优先级高的先出队。

优先级取决于一个f函数，每个节点都有对应的f值，指从起始节点到这个节点的最小cost.f越低，优先级越高，UCS会优先展开这些节点。

问题在于如何得知f，我们只能在搜索过程中得知从起始节点到某节点的可能花费，我们需要维护所有可能花费中的最小值，在这之后，如果再次搜索到这个节点且花费更高，那么就立即剪枝(即不做任何操作)，否则将此节点加入openlist重新搜索并更新f.

UCS是完备的，最优的，但时间复杂度较高

值得注意的是，USC由于以上操作，不再需要维护closedlist，只需维护f函数，也因此：


### 贪婪最佳优先搜索
在优先队列的基础上，改变优先级函数f，定义f为一个已知的先验函数h(称为启发式函数)，代表某节点到目标的估计花费，如直线距离等。

如果贪婪算法不维护closedlist：

是不完备(这不如UCS)，不最优的(启发式函数可能不符合实际)。

维护closedlist的贪婪最佳优先搜索是完备的，但仍然不保证最优。

### A*搜索
有一个先验函数h，代表某节点到终点的估计花费，又同时如UCS一样维护每个节点的cost函数g，令优先级函数为f = g + h，其中g在搜索过程中可能被更新。

A*搜索是完备的：类似UCS，如果两次搜索到同一节点，则比对f，若更高(大于等于)则剪枝，否则更新f并重新搜索。由于图有限，更新次数一定有限，所以总搜索量有限，因此完备。

A*搜索是否最优？这是一个优化类问题，优化h。

#### A*算法最优性——数学证明
我们从头思考$f$，$g$与$h$.
研究图$G$，记开始节点为$S$，目标节点为$E$，对$G$中每个节点$V$，都可以定义$f_{真}(V)$代表从$S$经过$V$到达$E$的所有路径中最短的实际成本，由于$G$联通，$f_{真}$良定义。

而对于整个问题，有一个全局最短路，记为$P\subset G$，显然$P$是一条没有重复的路径。
##### 命题1

$\forall V \in G, f_{真}(V)\geq f_{真}(S), 取等当且仅当V\in P$

于是，如果已知$f_{真}$，根本不用搜索，能直接给出最短路径。

一般我们不知道$f_{真}$，需要用$f$来估计。

##### 定义1

$g_{真}(V)$定义为从$S$到达$V$的所有路径中最短的实际成本

$h_{真}(V)$定义为从$V$到达$E$的所有路径中最短的实际成本

##### 命题2

$\forall V \in G, f_{真}(V)=g_{真}(V)+h_{真}(V)$

##### 定义2

$g_{t}(V)$定义为遍历过程中(状态t)已知的，$S$到达$V$的所有路径中，最小的成本

我们将$f_{真}$拆成$g_{真}+h_{真}$分别用$g$，$h$进行估计，因为实际搜索中，$g$比较好得到，在不断搜索中记录并更新就能得到g。

##### 命题3

$g_{t}(V)关于t不增，且\forall t，g_{t}(V) \leq g_{真}(V)$

##### 定理1
$\forall V \in G,若 h(V) \leq h_{真}(V)，则称h可接纳，此种情况下A*算法完备且最优(如果允许通过比较重新打开节点，否则不最优)$

##### 定义3
$对\forall V_{1},V_{2} \in G,定义D(V_{1},V_{2})为从V_{1}到V_{2}的真实最短路径成本$

##### 定理2
$若h满足三角不等式：h(V_{1})+D(V_{1},V_{2}) \leq h(V_{2}), 且h(E) = 0，则称h是一致的.一致蕴含可接纳，在图搜索中A*算法是完备且最优的，而且必定不会重新打开节点.$

定理证明详见相关文章。

#### 设计h
##### 支配
若对于可接纳的$h_{1}$，$h_{2}$有$h_{1} \geq h_{2}$，称$h_{1}$支配$h_{2}$，此时$h_{1}$严格更优。

##### 松弛法
对于原命题，我们可以取消一些限制，得到新命题，显然新命题的$h_{真}$可视为原问题的启发式函数。一般而言，这些启发式函数天然一致。
# 大班课: 局部搜索算法
基本思想: 从一个状态开始, 找状态估值函数最好的邻居状态, 直到找到局部最优解或达到最大迭代次数.

无需存储路径, 只需存储当前节点

可能情况:
- 全局极值
- 局部极值(不好)
- 平台(两边都更差, 不好)
- 肩状平台(一边差一边好)

        如何跳出平台或者局部极值点??
## 爬山法
### 最抖下降
每次找最好的邻居

有概率僵住(设定死循环上限)
### 平移
允许跳跃到另一个至少不会更差的状态
### 随机爬山
每次随机选一个更好的邻居

    有概率跳出局部最优, 但一般收敛更慢
### 第一选择爬山
随机一个邻居, 算估值, 不好就变, 换一个, 直到有一个更好的.

    不用存所有邻居的信息了
### 随机重启爬山
废了就随机找一个初始状态重来

    近似完备, 其实也很高效.
## 模拟退火
用'温度'表示往更差邻居跳的可能性. 还有一个容忍度用来表示可容忍的'差的程度'.

一开始温度高, 容易跳出局部极值; 之后温度越来越低, 用于收敛.

    以上两种算法在内存利用上有点交往过正, 其实可以再利用一些内存.

## 局部束搜索
一开始初始化k个不同状态, 找出所有邻居, 如果有目标则结束, 否则在所有这些邻居中找出前k个最好的进行下一轮.

    (这与k次重启爬山完全不同)

## 随机束搜索
不再最好的k个, 而是有某种方法增加随机性
## 遗传算法(随机束变种, 需要状态内有可细分重组的部分)
1) 初始状态种群
2) 评分选择成为父代概率
3) 繁殖, 交叉互换
4) 子代随即变异
5) 重复以上步骤, 直到达到终止条件

        难绷, 适合解决特定生物模拟问题...
## 连续空间中的局部搜索
### 离散化
### 梯度下降(包括随机重启, 退火等)

# 大班课: 强化学习
## 理论基础
使用奖励和惩罚可以改变智能体的行为.

随机奖励上瘾

强化学习一般处理动态问题(含时间序列数据), 但和RNN路子完全不同.

## 基础模型
两个主体
- 环境
- 智能体

一个时间步内, 环境给智能体当前状态信息, 与上一时间步的奖励; 智能体判断并作出决策, 改变环境状态.

详细点:
1) 初始状态
2) 当前玩家
3) 合法动作
4) 状态转移
5) 终止状态
6) 奖励
7) 全局策略(状态到动作的映射, 也是学习的目标)

## 状态估值表
全局策略的形式

类似搜索, 有概率选择更差的邻居(探索).
## 训练流程
### 初始化
显然赢的情形设为1, 输的设为0, 其余平均化设为0.5.
### 学习
贪心 + 探索
### 更新估值
多次学习后, 更新每个点获胜的概率, 使其更接近真实值.
## 扩展
策略可以按概率分布, 奖励也可以按概率给.

可以引入折扣因子($\gamma$)和累计收益($G$), 按累计收益指定策略

$$G = 𝑅_{1}+𝛾𝑅_{2}+𝛾^{2}𝑅_{3}+⋯=∑_{i = 1}^{T}𝛾^{i−1}𝑅_{i}$$

其中$𝑅_{i}$为第i步的奖励, 𝛾取值在0到1之间.

𝛾 = 0则退化为平凡贪心情形.
## 评价策略好坏
状态价值是一个函数, 描述从状态S按策略$\Pi$进行得到的累计收益.

动作价值则指从S做A后再按照$\Pi$行动的累计收益, 有时这个更好算, 也可以用这个评价.
## 寻找最佳策略的方式
以多臂老虎机为例
### 计算动作价值
说白了就是先验 + 尝试 = 后验
### 贪心与$\epsilon$-贪心
即贪心与概率贪心
### 乐观贪心
给出先验估值

也可用于鼓励探索
### UCB
把动作估值与新鲜程度做加权, 然后再找.
### 梯度下降
给每个状态下的每个动作一个优先级, 并计算平均奖励, 按照softmax概率选择一系列动作后, 更新动作优先级(梯度下降)

    总体而言, UCB在多臂老虎机中表现好
# 大班课: 具身智能
莫拉维克悖论: 人类觉得困难的, 机器学起来很简单; 人类觉得简单的, 机器学起来很困难.
## 算法支持
模仿学习 + 强化学习

大小脑协同框架:
- 大脑: 多模态model + data 
- 小脑: specific works

        模块化, 泛化性, 可解释


## 长程操作要求
- 任务规划
- 可操作区域感知
- 轨迹预测
## 数据来源
- 真机
- 仿真
- 网络
### 仿真
效果差
### 真机
- 基础遥操作
- **同构遥操作**
# 补充
1) 扩散模型: 正向扩散, 反向去噪
2) dropout a代表向前传播时, 有a的概率把神经元置0.
3) bagging并行同质, boosting串行同质, stacking串行异质.

