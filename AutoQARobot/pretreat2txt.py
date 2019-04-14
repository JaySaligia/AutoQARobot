import jieba
import jieba.analyse
import re
with open(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\traindata_new.txt', 'rb') as f:
    doc = f.read()
    doc_cut = jieba.cut(doc)
    result = ' '.join(doc_cut)
    result = result.encode('utf-8')
    result_tmp = result.decode('utf-8')
    filterstr = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”（）‘’：——！[\\]^_`{|}~的什么我有怎吗是自己]+' 
    result = re.sub(filterstr, '', result_tmp).encode('utf-8')
    with open(r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\qanda_after.txt', 'wb') as f_w:
        f_w.write(result)
    f.close()
    f_w.close()
    
        