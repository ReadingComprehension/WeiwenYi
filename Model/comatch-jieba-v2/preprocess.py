#coding=utf-8
import glob
import os
import json
import jieba
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings('ignore')

# build StopWordSet
StopWordsSet = []
SpecialcharSet = []
with open('StopWords.txt','r',encoding='gb18030') as fp:
    for line in fp.readlines():
        StopWordsSet.append(line.strip('\n'))
    StopWordsSet.append(" ")
    StopWordsSet.append("\"")
SpecialcharSet.append(" ")
SpecialcharSet.append("\"")


# wd_tokenize for passage
def wd_tokenize(text):
    segments_all = jieba.lcut(text, HMM=True, cut_all=False)
    segments = []
    for word in segments_all:
        if word not in StopWordsSet:
            segments.append(word)
    return segments

# wd_tokenize for query and ans
def wd_tokenize_qa(text):
    segments_all = jieba.lcut(text, HMM=True, cut_all=False)
    segments = []
    for word in segments_all:
        if word not in SpecialcharSet:
            segments.append(word)
    return segments

def answer_index(answer,options):
    if answer == options[0]:
        return 0
    elif answer == options[1]:
        return 1
    else:
        return 2
'''
将原始json中的数据分词分句,并且将答案映射成index形式,生成新.json文件存储在data/RC/sequence中
'''

def preprocess(task):
    print('Preprocessing the dataset ' + task + '...')
    data_names = ['train','valid','test']
    for data_name in data_names:
        data_all = []
        path = os.path.join('data', task, data_name)
        with open(path + '.json', 'r', encoding='utf-8') as fpr:
            for line in fpr.readlines():
                data_raw = json.loads(line)
                instance = {}
                instance['q_id'] = data_raw['query_id']
                if data_name != 'test':
                    instance['ground_truth'] = answer_index(data_raw['answer'],data_raw['alternatives'].split('|'))
                # without stopwords
                # instance['article'] = [wd_tokenize(s.strip()) for s in sent_tokenize(data_raw['passage'])]
                # with stopwords
                instance['article'] = [wd_tokenize_qa(s.strip()) for s in sent_tokenize(data_raw['passage'])]
                instance['question'] = wd_tokenize_qa(data_raw['query'].strip())
                instance['options'] = [wd_tokenize_qa(option.strip()) for option in data_raw['alternatives'].split('|')]

                data_all.append(instance)
                if len(data_all) % 1000 == 0:
                    print(len(data_all))
        with open(os.path.join('data', task, 'sequence', data_name) + '.json', 'w', encoding='utf-8') as fpw:
        # with open(os.path.join('data', task, 'sequenceAfterWashP', data_name)+'.json', 'w', encoding='utf-8') as fpw:
            json.dump(data_all, fpw,ensure_ascii=False)

if __name__ == '__main__':
    preprocess('RC')
