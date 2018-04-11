import tensorflow as tf

foo = tf.constant([1,2,3,4,5,6])

sess = tf.Session()
print(sess.run(foo[2:-2]))
