import tensorflow as tf
import numpy as np

embedding_dim = 24
seq_length = 8
num_classes = 55
num_filters = 256
kernel_size = 5 
hidden_dim = 128
dropout_keep_prob = 0.5
learning_rate = 1e-3
batch_size = 32
max_steps = 100000
def main():
    #加载预处理数据
    processed_data = np.load(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\processed_data.npy")
    training_data = processed_data[0]
    training_labels = processed_data[1]
    n_training_example = len(training_data)
    validation_data = processed_data[2]
    validation_labels = processed_data[3]
    testing_data = processed_data[4]
    testing_labels = processed_data[5]
    print("%d training examples. %d validation examples and %d testing examples." %(n_training_example, len(validation_labels), len(testing_labels)))
    #定义输入
    data = tf.placeholder(tf.float32, [None, seq_length, embedding_dim], name = 'input_data')
    labels = tf.placeholder(tf.int64, [None], name = 'labels')
    with tf.name_scope('cnn_layer'):
        conv = tf.layers.conv1d(data, num_filters, kernel_size, name = 'conv')
        gmp = tf.reduce_max(conv, reduction_indices=[1], name = 'gmp')
    with tf.name_scope('fully_connnected_layer'):
        fc = tf.layers.dense(gmp, hidden_dim, name = 'fc1')
        fc = tf.contrib.layers.dropout(fc, dropout_keep_prob)
        fc = tf.nn.relu(fc)
        logits = tf.layers.dense(fc, num_classes, name = 'fc2')
        predict = tf.argmax(tf.nn.softmax(logits), 1)
    with tf.name_scope('losses'):
        tf.losses.softmax_cross_entropy(tf.one_hot(labels, num_classes), logits, weights=1.0)
        train_step = tf.train.RMSPropOptimizer(learning_rate).minimize(tf.losses.get_total_loss())
        
    with tf.name_scope('accuracy'):
        correct_pred = tf.equal(tf.arg_max(logits, 1), labels)
        evaluation_step = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    saver = tf.train.Saver()
    tf.add_to_collection('prediction', predict)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        print("Begin training")
        
        start = 0
        end = batch_size
        for i in range(max_steps):
            sess.run(train_step, feed_dict={
                data: training_data[start:end],
                labels: training_labels[start:end]})
            print('Step %d' %(i))
            if i % 30 == 0 or i + 1 == max_steps:
                saver.save(sess, r'C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\checkpoint\textcnn.cpkt', global_step=i)
                validation_accuracy = sess.run(evaluation_step, feed_dict={
                    data: validation_data, labels:validation_labels})
                print('Step %d: Validation accuracy = %.1f%%' % (i, validation_accuracy * 100.0))
                start = end
                if start == n_training_example:
                    start = 0

                end = start + batch_size
                if end > n_training_example:
                    end = n_training_example
            test_accuracy = sess.run(evaluation_step, feed_dict={
                data: testing_data, labels: testing_labels})
        print('Final test accuracy = %.1f%%' % (test_accuracy * 100))

main()