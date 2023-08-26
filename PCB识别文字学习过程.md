通过随机数生成10000份样本语料库

![image-20221210190542578](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210190542578.png)

<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210185454029.png" alt="image-20221210185454029" style="zoom:33%;" />

生成对应的数据集：

![image-20221210190606510](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210190606510.png)



## 1.评估预训练模型精度：

![image-20221210190718040](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210190718040.png)

![image-20221210190849673](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210190849673.png)

**检测准确率：0.7221041445270988**

2.预训练模型+fine-tune

使用预设值好的6400张训练照片与1600评估照片的数据集来训练、fine-tune、评估模型。

训练中：

![image-20221210192822327](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221210192822327.png)

评估结果：

文字识别评估训练模型：

![image-20221211124423964](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221211124423964.png)

# 二、检测与识别问题

**待完成**：

- [ ] 1.将残缺样本（非完整文本、遮挡文本）去除掉之后，完整文本段的识别准确率是否可以达到100%？（设定一个阈值来分析错误样本）2.可以合成和电路图字体字号相似的样本
- [ ] 确定好缺失样本部分的位置，有目的的增加样本的多样性。
- [ ] 可靠性分析（方向）
- [ ] 可以先根据错误样本做识别训练，后做检测。
- [ ] 找出不可靠的样本（看着是完整样本，但是会识别错误）

**目前效果**：

去除残缺样本检测成功率：**99.669%**（基本满足预期指标）、识别成功率：**92.911%**

<img src="F:\OCR_Project\results\1.png" style="zoom:33%;" />

**错误样本汇总：**

**scores:**	

**0.5~0.8（accuracy：25.53%）该范围的样本数是： 94:** 

1.*完整字符识别问题*：accuracy：

纵向文本：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229124715331.png" alt="image-20221229124715331" style="zoom:50%;" /> 数字不完整：![image-20221229124940774](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229124940774.png) 错误检测识别：![image-20221229125010952](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229125010952.png) 

同段字符重复识别检测：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229125113395.png" alt="image-20221229125113395" style="zoom:50%;" /> 翻转数字片段漏检：![image-20221229125819711](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229125819711.png)

2.*残缺字符识别问题*：accuracy：

字符遮挡造成的不准确匹配识别：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229125431682.png" alt="image-20221229125431682" style="zoom:50%;" />

漏检少检：

<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229125518042.png" alt="image-20221229125518042" style="zoom:50%;" />

**0.8~0.9** **（accuracy：25.53%）该范围的样本数是： 140:**

1.*完整字符识别问题*：accuracy：

 对于D13旋转文本识别错误：![image-20221229171718351](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171718351.png)  **模糊**密集文本识别结果不好：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171917487.png" alt="image-20221229171917487" style="zoom:50%;" />  

检测区域完整但是内容检测错误：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171237202.png" alt="image-20221229171237202" style="zoom:50%;" /> 旋转90°文本识别不佳：![image-20221229171620005](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171620005.png)

2.*残缺字符识别问题*：accuracy：

漏检少检（检测区域不完整）：![image-20221229171126283](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171126283.png) ![image-20221229171201125](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171201125.png) 



对于FPGA字符识别一直错误：![image-20221229171438750](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229171438750.png) 

**0.9~0.99** **（accuracy：94.843%）该范围的样本数是： 543:**

1.*完整字符识别问题*（490）：错误数量（5）accuracy：98.979%

错误识别：<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229173007717.png" alt="image-20221229173007717" style="zoom:50%;" />  ![image-20221229173107605](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229173107605.png) 

2.*残缺字符识别问题*（53）：错误数量（23）accuracy：56.603%

错误识别： ![image-20221229172652066](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229172652066.png)  ![image-20221229172702618](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229172702618.png)  <img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229172716871.png" alt="image-20221229172716871" style="zoom:50%;" /> ![image-20221229172735045](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229172735045.png)  ![image-20221229172742654](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229172742654.png)  

**0.99~1** **（accuracy：25.53%）该范围的样本数是： 1438:**

1.*完整字符识别问题*：accuracy：99.7%

**out、_B1、D1识别一直出错**<img src="C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229175109079.png" alt="image-20221229175109079" style="zoom:50%;" /> ![image-20221229175205658](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229175205658.png)  ![image-20221229175452549](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229175452549.png)

2.*残缺字符识别问题*：accuracy：94.121%

误检：![image-20221229174553508](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229174553508.png) 

![image-20221229175655975](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229175655975.png) 





### 检测模型问题：

​	

1. 检测不完整导致识别结果不准确：

   

   ![image-20221229180259723](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229180259723.png) ![image-20221229180308176](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229180308176.png) 

   

2. 完整文本极少数的漏检：![image-20221229180444535](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229180444535.png) 

3. 残缺文本的漏检：![image-20221229180510665](C:\Users\m\AppData\Roaming\Typora\typora-user-images\image-20221229180510665.png) 

