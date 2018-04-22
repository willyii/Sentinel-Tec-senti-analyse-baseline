#!/usr/bin/env python
# -*- coding: utf-8  -*-
#去除停用词
import codecs,sys

#对一句话进行去停词处理
def stopWord_sent(sentence):
    '''
    :param sentence: 需要进行停词处理的句子
    :return: 去除停词后的句子
    '''
    stopkey = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]#加载停词
    sentence_stopword = delstopword(sentence, stopkey)
    return sentence_stopword

#对一个文档进行停词处理
def stopWord_doc(sourceFile,targetFile):
    '''
    :param sourceFile: 需要进行停词处理的文档
    :param targetFile: 处理后需要保存的文档
    :return:
    '''
    stopkey = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]#加载停词

    sourcef = codecs.open(sourceFile, 'r', encoding='utf-8')
    targetf = codecs.open(targetFile, 'w', encoding='utf-8')
    print ('open source file: '+ sourceFile)
    print ('open target file: '+ targetFile)
    lineNum = 1
    for line in sourcef.readlines():#对行进行操作，同时写入文件
        print ('---processing ',lineNum,' article---')
        sentence = delstopword(line,stopkey)
        #print sentence
        targetf.writelines(sentence + '\n')       
        lineNum = lineNum + 1

    print ('well done.')
    sourcef.close()
    targetf.close()

#删除停用词
def delstopword(line,stopkey):
    '''
    :param line: 需要删除停词的行
    :param stopkey: 停词列表
    :return: 删除停词后的行
    '''
    wordList = line.split(' ')          
    sentence = ''
    for word in wordList:
        word = word.strip()
        if word not in stopkey:
            if word != '\t':
                sentence += word + " "
    return sentence.strip()

