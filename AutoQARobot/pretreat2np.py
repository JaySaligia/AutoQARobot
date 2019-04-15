import os.path
import numpy as np
import tensorflow as tf
import jieba
import re
from gensim.models import word2vec
#将数据根据分词后转换为词向量存储为np格式
training_data = []
training_labels = []
testing_data = []
testing_labels = []
validation_data = []
validation_labels = []
wordvec_dim = 24
seq_len = 8

model = word2vec.Word2Vec.load(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda.model")
with open(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\traindata_new.txt') as f:
    lines = f.readlines()
    print(lines)
    count = 0
    for line in lines:
        if not line == '\n':
            print("正在处理第" + str(count) + "个问题")
            count += 1
            label = int(line.split('.')[0]) - 1
            filterstr = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”（）‘’：——！[\\]^_`{|}~的什么我有怎吗是自己了该\n]+' 
            line = re.sub(filterstr,'', line)
            line = re.sub('武汉大学', '武大', line)
            line = re.sub('武大', '学校', line)
            jieba.load_userdict(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\dict.txt')
            cut = jieba.cut(line)
            linelist = ' '.join(cut).split(' ')                
            datamritix = np.zeros((seq_len, wordvec_dim), dtype=float)
            #high = min(len(linelist), seq_len)
            #for i in range(high):
            #    if linelist[i] in model:
            #        row = model[linelist[i]]
            #    else:
            #       row = np.zeros(wordvec_dim, dtype=float)
            #   datamritix[i] = row
            for i in range(seq_len):
                k = np.random.randint(len(linelist))
                if linelist[k] in model:
                    row = model[linelist[k]]
                else:
                    row = np.zeros(wordvec_dim, dtype=float)
                datamritix[i] = row
            training_data.append(datamritix)
            training_labels.append(label)
            chance = np.random.randint(100)
            if chance < 10:
                 testing_data.append(datamritix)
                 testing_labels.append(label)
            elif chance < 20:
                 validation_data.append(datamritix)
                 validation_labels.append(label)
    state = np.random.get_state()
    np.random.shuffle(training_data)
    np.random.set_state(state)
    np.random.shuffle(training_labels)
    processed_data = np.asarray([training_data, training_labels, validation_data, validation_labels, testing_data, testing_labels])        
    np.save(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\processed_data.npy",processed_data)                    

                    