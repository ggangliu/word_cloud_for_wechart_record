import os

os.system("pyinstaller --add-data C:\Python27\Lib\site-packages\wordcloud\stopwords;.\wordcloud -F generate_wordcloud.py")
os.system("copy config.ini dist\config.ini")
os.system("md dist\config")
os.system("copy config\* dist\config")