#!/usr/bin/env python
# -*- coding: utf-8  -*-

#将已经分词好并且已经去除停词的文档整理为能够进行训练的文档
import codecs

def prepare_data(sourceFile, targetFile, category):
    '''
    :param sourceFile: 需要进行整理的文档
    :param targetFile: 整理后的文档
    :param category: 该文档所属类别，整理后，每一句话前面都会机上所属类别的标签
    :return:
    '''
    sentences = []
    sourcef = codecs.open(sourceFile, 'r', encoding='utf-8')
    targetf = codecs.open(targetFile, 'w', encoding='utf-8')
    print ('open source file: '+ sourceFile)
    print ('open target file: '+ targetFile)

    #往每一句前面加上标签
    for line in sourcef.readlines():
        sentences.append("__label__" + str(category) + " " + line.split("\t")[0].strip('\n') )
    sourcef.close()

    #写入目标文件
    for sentence in sentences:
        targetf.writelines(sentence)
    targetf.close()