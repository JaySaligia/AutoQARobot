import logging
import os
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda_after.txt') 

model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=8,size=24)

model.save(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda.model")

