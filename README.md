# word\_cloud\_for\_wechart\_record
Generates a word cloud image from a text file and a mask picture.

根据一个文本文件和一个图片,生成一个词云图片


## How to

1. Clone this repository to your local machine using either SSH or HTTPS:  
    - `git@github.com:ggangliu/word_cloud_for_wechart_record.git`  
    - `https://github.com/ggangliu/word_cloud_for_wechart_record.git`

2. Run `python generate_wordcloud.py`.

3. Inform the following files paths as requested:
    - Text file; 
    - 中英文文本文件，例如简历  
    
    - Mask picture(optional);  
    
    - 一个生成词云的图片，例如心形，可选
    
    - Background picture (optional); 
    
    - 词云的背景图片，可选  
    
    - Font path (Required only on Windows); 
    
    - 字体路径，windows系统下是不设置的话，用程序的默认字体'C:\Windows\Fonts\STLITI.TTF'


The output file will be saved to the same directory as the script and will be called `wordcloud.png`.

生成的词云图片文件和脚本保存在同一个目录下，名字叫“wordcloud.png”

