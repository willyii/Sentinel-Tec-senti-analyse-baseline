#!/usr/bin/env python
# -*- coding: utf-8  -*-

#对文档进行jieba分词
import jieba
import jieba.analyse
import codecs,sys,string,re

# 清洗文本，去除文中的符号等
def clearTxt(line):
    '''
    :param line: 需要进行符号清洗的句子
    :return: 符号清洗后的句子
    '''
    if line != '':
        line = line.strip()
        line = re.sub("[a-zA-Z0-9]","",line)
        #去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+", "",line)
    return line


#文本切割
def sent2word(line):
    '''
    :param line: 需要进行分词的句子
    :return: 分词后的句子
    '''
    segList = jieba.cut(line,cut_all=False)
    segSentence = ''
    for word in segList:
        if word != '\t':
            segSentence += word + " "
    return segSentence.strip()

#对整个文档进行预处理
def preprocess_doc(sourceFile, targetFile ):
    '''
    :param sourceFile: 需要进行分词预处理的文档
    :param targetFile: 分词预处理后的文档
    :return:
    '''
    source = codecs.open(sourceFile, 'r', encoding='utf-8')
    target = codecs.open(targetFile, 'w', encoding='utf-8')
    print ('open source file: '+ sourceFile)
    print ('open target file: '+ targetFile)

    #对每一句进行清洗，再分词，再写入目标文件
    lineNum = 1
    for line in source.readlines():
        print('---processing ',lineNum,' article---')
        line = clearTxt(line)
        seg_line = sent2word(line)
        target.writelines(seg_line + '\n')
        lineNum = lineNum + 1

    print ('well done.')
    source.close()
    target.close()

#对一句话进行清洗分词预处理
def preprocess_sent(sentence ):
    '''
    :param sentence: 需要进行预处理的句子
    :return: 清洗，分词后的句子
    '''
    sentence_clear = clearTxt(sentence)
    seg_sentence = sent2word(sentence_clear)
    return seg_sentence