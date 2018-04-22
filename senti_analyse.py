#!/usr/bin/env python
# -*- coding: utf-8  -*-
#情感极性分析
import fasttext
import prepare_data
import preprocess
import stopwords
import codecs

#情感极性分析类
class senti_analyse(object):

    def __init__(self, model_path = 'model/classifier.model.bin'):#默认加载已有模型
        if model_path:
            self.model = fasttext.load_model(model_path, label_prefix = '__label__')
        if model_path == None:
            self.model = None

    #对一句话进行情感分析
    def analyse_sent(self, sentence):
        sentence = preprocess.preprocess_sent(sentence)
        sentence = stopwords.stopWord_sent(sentence)
        ans = self.model.predict([str(sentence)])
        return ans[0]

    #对一个文档进行情感极性分析
    def analyse_doc(self, testFile):
        #定义清洗分词后的文档名，并进行清洗分词预处理
        targetfilename1 = testFile.split('.')[0] + '_cut_split.txt'
        preprocess.preprocess_doc(testFile, targetfilename1)

        #定义去停词后的文档名，并进行去停词处理
        targetfilename2 = targetfilename1.split('.')[0] + '_stop.txt'
        stopwords.stopWord_doc(targetfilename1, targetfilename2)

        #重新整理句子，并进行预测
        sentences = []
        for line in open(targetfilename2,"r"):
            sentences.append(line)
        ans = self.model.predict(sentences)
        return ans

    #对模型进行训练（仅当 self.model == None 的时候可以使用）
    def train(self, trainFile, category, process = True):
        '''
        :param trainFile: 进行训练的文档
        :param category: 该文档所属类别，从cate_dict中选择
        :param process: 该输入文档是否需要预处理
        :return:
        '''
        if process == True:
            #定义清洗分词后的文档名，并进行清洗分词预处理
            targetfilename1 = trainFile.split('.')[0] + '_cut_split.txt'
            preprocess.preprocess_doc(trainFile, targetfilename1)

            # 定义去停词后的文档名，并进行去停词处理
            targetfilename2 = targetfilename1.split('.')[0] + '_stop.txt'
            stopwords.stopWord_doc(targetfilename1, targetfilename2)

            #对预处理后的文档加上标签
            trainFile = targetfilename1.split('.')[0] + '_labeled.txt'
            prepare_data.prepare_data(targetfilename2, trainFile, category)

        #训练
        classifier = fasttext.supervised(trainFile,'model/classifier2.model' ,label_prefix='__label__')


    #输入测试集合，对模型进行评估
    def test_doc(self, testFile, category = None, process = True):
        '''
        :param trainFile: 进行测试的文档
        :param category: 该文档所属类别，从cate_dict中选择
        :param process: 该输入文档是否需要预处理
        :return: 测试结果
        '''

        if process == True:
            #定义清洗分词后的文档名，并进行清洗分词预处理
            targetfilename1 = testFile.split('.')[0] + '_cut_split.txt'
            preprocess.preprocess_doc(testFile, targetfilename1)

            # 定义去停词后的文档名，并进行去停词处理
            targetfilename2 = targetfilename1.split('.')[0] + '_stop.txt'
            stopwords.stopWord_doc(targetfilename1, targetfilename2)

            #对预处理后的文档加上标签
            testFile = targetfilename1.split('.')[0] + '_labeled.txt'
            prepare_data.prepare_data(targetfilename2, testFile, category)

        #测试
        ans = self.model.test(testFile)
        return ans


if __name__ == '__main__':
    test_data = "data/fasttext_test.txt"
    model = senti_analyse()
    ans = model.test_doc(test_data , None,  process = False)
    print('P@1:', ans.precision)
    print('R@1:', ans.recall)
    print('Number of examples:', ans.nexamples)