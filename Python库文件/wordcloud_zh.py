import jieba
from wordcloud import WordCloud
def wordcloud(text,output):
    WordCloud(font_path="msyh.ttc").generate("".join(jieba.lcut(text))).to_file(output)
