#!/usr/bin/python
#coding=utf-8

#统计文件中单词的出现频率

count = 10
data = []
words = []

#对文本的每一行计算词频的函数
def processLine(line, wordCounts):
    #用空格替换标点符号
    line = replacePunctuations(line)
    #从每一行获取每个词
    words = line.split() 
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
 
#空格替换标点的函数
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, " ")
    return line
 
def main():
    #用户输入一个文件名
    filename = raw_input("enter a filename:")
    infile = open(filename, "r")
     
    #建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)
         
    #从字典中获取数据对
    pairs = list(wordCounts.items())
    #列表中的数据对交换位置,数据对排序
    items = [[x,y]for (y,x)in pairs] 
    items.sort() 
 
    #输出count个数词频结果
    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
         
    infile.close()
    print words
    print data
#调用main()函数
if __name__ == '__main__':
    main()
