# -*- coding: utf-8 -*-

#导入wordcloud模块和matplotlib模块
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud


def generate_wordcloud(words_file, mask_pic, bg_pic, font_file=None):
    #读取一个txt文件
    # Context managers automatically close the file after all operations finished
    with open(words_file, 'r') as f:
        text = f.read()

    #读入背景图片
    mask_pic = np.array(Image.open(mask_pic))

    # Mode RGBA and background color None makes the background transparent, that way we can paste the resulting image
    # into another one, which will be the background
    wordcloud = WordCloud(mask=mask_pic, background_color=None, scale=1.5, mode='RGBA').generate_from_text(text)

    #显示词云图片
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

    #保存图片
    # Using .png to support transparency
    wordcloud.to_file('foreground.png')

    foreground = Image.open('foreground.png')
    background = Image.open(bg_pic)

    width, height = foreground.size
    background = background.resize((width, height), Image.ANTIALIAS)

    background.paste(foreground, (0,0), foreground)
    background.show()

    background.save('wordcloud.png')


if __name__ == '__main__':
    words_file = raw_input('File to read text from: ')
    if not words_file:
        words_file = 'how to choose the first open source project.txt'
    
    mask_pic = raw_input('Mask picture path: ')
    if not mask_pic:
        mask_pic = 'human.png'

    bg_pic = raw_input('Background picture path: ')
    if not bg_pic:
        bg_pic = 'background.jpg'

    font_file = raw_input('Custom font path (optional): ')

    generate_wordcloud(words_file, mask_pic, bg_pic, font_file)