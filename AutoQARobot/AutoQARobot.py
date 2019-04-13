import os.path
import numpy as np
import tensorflow as tf
import jieba
import re
from gensim.models import word2vec


model = word2vec.Word2Vec.load(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda.model")
def test(seq):
    filterstr = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、\\n…【】《》？“”（）‘’：——！[\\]^_`{|}~]+' 
    seq = re.sub(filterstr,'', seq)
    cut = jieba.cut(seq)
    linelist = ' '.join(cut).split(' ')
    print("分词结果为：" + ' '.join(linelist))
    print(linelist)
    datamritix = np.zeros((12, 24), dtype=float)
    high = min(len(linelist), 12)
    for i in range(high):
        if linelist[i] in model:
            row = model[linelist[i]]
        else:
            row = np.zeros(24, dtype=float)
        datamritix[i] = row

    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\checkpoint\textcnn.cpkt-999.meta')
        new_saver.restore(sess, r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\checkpoint\textcnn.cpkt-999')
        y = tf.get_collection('prediction')
        graph = tf.get_default_graph()
        data = graph.get_operation_by_name('input_data').outputs[0]
        datamritix = datamritix[np.newaxis, :]
        ret = sess.run(y, feed_dict = {data: datamritix})[0][0]
        print("匹配结果为：" + str(ret))

test("我的水卡丢了该去哪儿补？")
    
