import sys
text = sys.stdin.read()
words = list(text)
word_count = len(words)
print('WordCount: ', word_count)


# 如何调用
# cat news.txt | python3 计算文档中单词个数.py
