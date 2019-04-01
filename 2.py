import tensorflow as tf
session=tf.Session()
hello=tf.constant("Hello")

a=tf.constant([1.0,2.0], name="a")
b=tf.constant([3.0,4.0], name="b")
c=a+b
print(a.graph)

