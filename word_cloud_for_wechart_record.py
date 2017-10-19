# -*- coding: utf-8 -*-

#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#读取一个txt文件
text = open('how to choose the first open source project.txt','r').read()

#读入背景图片
bg_pic = np.array(Image.open('human.png'))

#生成词云
wordcloud = WordCloud(mask=bg_pic,background_color='black',scale=1.5, font_path=r'C:\Windows\Fonts\STHUPO.TTF').generate_from_text(text)

#显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

#保存图片
wordcloud.to_file('test.jpg')