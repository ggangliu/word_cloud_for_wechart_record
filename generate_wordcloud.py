# -*- coding: utf-8 -*-

#import wordcloud and matplotlib module
import numpy as np
#import matplotlib.pyplot as plt
import os
import sys
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import ConfigParser

def get_config_from_file(config_file='config.ini'):
    #Get config information from config_file, default it included in ./config/config.ini
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    words_file = cf.get("base_config", "words_file")
    mask_pic   = cf.get("base_config", "mask_pic") if cf.has_option("base_config", "mask_pic") else None
    bg_pic     = cf.get("base_config", "bg_pic")  if cf.has_option("base_config", "bg_pic") else None
    font_file  = cf.get("window_config", "font_file") if cf.has_section("window_config") else None
    
    return words_file, mask_pic, bg_pic, font_file

def generate_wordcloud(words_file, mask_pic=None, bg_pic=None, font_file=r'C:\Windows\Fonts\STLITI.TTF'):
    #Read a txt file                                                                     
    # Context managers automatically close the file after all operations finished
    #font_file = None
    print "%s, %s, %s, %s" % (words_file, mask_pic, bg_pic, font_file)

    with open(words_file, 'r') as f:
        text = f.read()
        word_jieba = jieba.cut(text,cut_all=True)
        word_split = " ".join(word_jieba)

    if mask_pic:
        #读入背景图片
        mask_pic = np.array(Image.open(mask_pic))
        wordcloud = WordCloud(mask=mask_pic, background_color=None, scale=1.5, mode='RGBA', stopwords=STOPWORDS, font_path=font_file).generate(word_split)
        
    # Mode RGBA and background color None makes the background transparent, that way we can paste the resulting image
    # into another one, which will be the background
    else:
        wordcloud = WordCloud(max_words=200,width = 1200,height=800, mode='RGBA', background_color=None, stopwords=STOPWORDS, font_path=font_file).generate(word_split)
    

    # 保存图片
    # Using .png to support transparency
    wordcloud.to_file('wordcloud.png')

    #显示词云图片
    if not bg_pic:
        Image.open('wordcloud.png').show()
    else:
        foreground = Image.open('wordcloud.png')
        background = Image.open(bg_pic)

        width, height = foreground.size
        background = background.resize((width, height), Image.ANTIALIAS)

        background.paste(foreground, (0,0), foreground)
        background.show()
        background.save('wordcloud.png')


if __name__ == '__main__':
    words_file, mask_pic, bg_pic, font_file = get_config_from_file("config.ini")
    generate_wordcloud(words_file, mask_pic, bg_pic, font_file)