import tensorflow as tf
hello = tf.constant('Hello, you successfully installed TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
