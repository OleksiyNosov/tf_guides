# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

def puts(value):
  print(value.eval())
  print()

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())

  foo = tf.constant([[71, 72, 73, 74, 75, 76], [11, 13, 17, 20, 21, 30]])

  puts(foo)

  puts(tf.reshape(foo, [-1]))

  puts(tf.reshape(foo, [6, 2]))

  puts(tf.reshape(foo, [3, 4]))

  puts(tf.argmax(input = tf.reshape(foo, [-1]), axis = 0))

  puts(tf.argmax(input = foo, axis = 1))
