# -*- coding: utf-8 -*-

#export wordcloud and matplotlib module
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image
from wordcloud import WordCloud
import ConfigParser

def get_config_from_file(config_file='./config/config.ini'):
    #Get config information from config_file, default it included in ./config/config.ini
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    words_file = cf.get("base_config", "words_file")
    mask_pic   = cf.get("base_config", "mask_pic")
    bg_pic     = cf.get("base_config", "bg_pic")
    font_file  = None

    if "window_config" in cf.sections():
        #font_file =  cf.get("window_config", "font_file") #This line can't be to works, how to give a windows path to font_file, like as r'C:\Windows\Fonts\COOPBL.TTF'
        font_file = r'C:\Windows\Fonts\COOPBL.TTF' #This line is temporary, can be delete if above line can be work

    return words_file, mask_pic, bg_pic, font_file

def generate_wordcloud(words_file, mask_pic, bg_pic=None, font_file=r'C:\Windows\Fonts\COOPBL.TTF'):
    #Read a txt file
    # Context managers automatically close the file after all operations finished
    print "%s, %s, %s, %s" % (words_file, mask_pic, bg_pic, font_file)

    with open(words_file, 'r') as f:
        text = f.read()

    #读入背景图片
    mask_pic = np.array(Image.open(mask_pic))

    # Mode RGBA and background color None makes the background transparent, that way we can paste the resulting image
    # into another one, which will be the background
    if not font_file:
        wordcloud = WordCloud(mask=mask_pic, background_color=None, scale=1.5, mode='RGBA').generate_from_text(text)
    else:
        wordcloud = WordCloud(mask=mask_pic, background_color=None, scale=1.5, mode='RGBA', font_path=font_file).generate_from_text(text)

    #显示词云图片
    if None == bg_pic:
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()

    #保存图片
    # Using .png to support transparency
    wordcloud.to_file('wordcloud.png')

    if bg_pic:
        foreground = Image.open('wordcloud.png')
        background = Image.open(bg_pic)

        width, height = foreground.size
        background = background.resize((width, height), Image.ANTIALIAS)

        background.paste(foreground, (0,0), foreground)
        background.show()
        background.save('wordcloud.png')


if __name__ == '__main__':
    words_file, mask_pic, bg_pic, font_file = get_config_from_file("./config/config.ini")
    generate_wordcloud(words_file, mask_pic, bg_pic, font_file)