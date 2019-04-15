import os.path
import numpy as np
import tensorflow as tf
import jieba
import re
from gensim.models import word2vec

wordvec_dim = 24
seq_len = 8
model = word2vec.Word2Vec.load(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda.model")
def test(seq):
    filterstr = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”（）‘’：——！[\\]^_`{|}~的什么我有怎吗是自己了该]+' 
    seq = re.sub(filterstr,'', seq)
    seq = re.sub('武汉大学', '武大', seq)
    seq = re.sub('武大', '学校' , seq)
    jieba.load_userdict(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\dict.txt')
    cut = jieba.cut(seq)
    linelist = ' '.join(cut).split(' ')
    print("分词结果为：" + ' '.join(linelist))
    print(linelist)
    datamritix = np.zeros((seq_len, wordvec_dim), dtype=float)
    high = min(len(linelist), seq_len)
    for i in range(high):
        if linelist[i] in model:
            row = model[linelist[i]]
        else:
            row = np.zeros(wordvec_dim, dtype=float)
        datamritix[i] = row

    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\checkpoint\textcnn.cpkt-9999.meta')
        new_saver.restore(sess, r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\checkpoint\textcnn.cpkt-9999')
        y = tf.get_collection('prediction')
        graph = tf.get_default_graph()
        data = graph.get_operation_by_name('input_data').outputs[0]
        datamritix = datamritix[np.newaxis, :]
        ret = sess.run(y, feed_dict = {data: datamritix})[0][0]
        print("匹配结果为：" + str(ret))

#with open(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\traindata_new.txt") as f:
#    for i in range(100):
#        line = f.readline()
#        test(line)
#    f.close()
test("怎么缴纳学费")