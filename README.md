# Sentinel Tec senti-analyse-baseline
该模型能够对用户的评价进行分析，来判断该判断属于正面评价还是负面评价。
该模型基于fasttext进行分类。不过尚未进行调参，应该能够进一步提高效果


## 文件列表:

Preprocess.py: 对一个输入的文档或句子进行清洗和分词预处理
Stopwords.py: 对一个输入的文档或句子进行删除停词的处理
prepare_data.py: 如果输入的数据集目的是为了进行测试或者训练，需要对删除停词后的数据集进行该处理
senti_analyse.py: 一个模型，可以进行一句话或者一个文档的情感分析，也可以从头训练一个模型，或者对模型进行评估

## data:

stopWord.txt: 停词表，可更换
酒店评论-6000: 目前模型的训练集和测试集来源
fasttext_test.txt: 目前模型的测试集合，在该集合上，准确率为0.8717434869739479
Fasttext_train.txt: 目前模型的测试集合，训练后，在该集合上的准确率为0.9185602617705871

## Model:

训练好的分类模型