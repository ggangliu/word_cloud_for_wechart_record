# -*- coding: utf-8 -*-

#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#读取一个txt文件
# Context managers automatically close the file after all operations finished
with open('how to choose the first open source project.txt', 'r') as f:
    text = f.read()

#读入背景图片
mask_pic = np.array(Image.open('human.png'))

# Mode RGBA and background color None makes the background transparent, that way we can paste the resulting image
# into another one, which will be the background
wordcloud = WordCloud(mask=mask_pic, background_color=None, scale=1.5, mode='RGBA', font_path=r'C:\Windows\Fonts\STHUPO.TTF').generate_from_text(text)

#显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

#保存图片
# Using .png to support transparency
wordcloud.to_file('test.png')

foreground = Image.open('test.png')
background = Image.open('background.jpg')

background.paste(foreground, (0,0), foreground)
background.show()

background.save('test_with_bg.png')
