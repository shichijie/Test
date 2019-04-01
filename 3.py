import tensorflow as tf 

a=tf.constant([1,2], name="a")
b=tf.constant([3,4], name="b")
c=a+b
#hello=tf.constant("Hello world")
ss=tf.Session()
print(c)
print(ss.run(c))