# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

mnist     = input_data.read_data_sets('./data/mnist/', one_hot=True)

pixels    = mnist.train.images.shape[1]
nums      = mnist.train.labels.shape[1]
pixel_wh  = int( np.sqrt( pixels ) )

x = tf.placeholder( tf.float32, shape=(None, pixels), name='x' )

def makeWeightVariable( shape, name ):
  init_W  = tf.truncated_normal( shape, stddev=0.1 )
  W       = tf.Variable( init_W, name='W_'+name )
  return W

def makeBiasVariable( shape, name ):  
  init_b  = tf.constant( 0.1, shape=[shape] )
  b       = tf.Variable( init_b, name='b_' + name )
  return b

def makeConv2d( x, W, name ):
  conv2d  = tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME', name='conv_'+name )
  return conv2d

with tf.name_scope('conv1') as scope:
  W       = makeWeightVariable( [5, 5, 1, 32 ], 'conv1' )
  b       = makeBiasVariable( 32, 'conv1' )
  x_imgs  = tf.reshape( x, (-1, pixel_wh, pixel_wh, 1 ) )
  h_conv1 = tf.nn.relu( makeConv2d( x_imgs, W, 'conv1' ) + b )

def makeMaxPooling( x ):
  return tf.nn.max_pool( x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME' )

with tf.name_scope('pool1') as scope:
  h_pool1 = makeMaxPooling( h_conv1 )

name_conv2 = 'conv2'
with tf.name_scope(name_conv2) as scope:
  # [h, w, 입력채널수=이전단계의출력채널수, 최종 출력채널수]
  W_conv2 = makeWeightVariable( [5, 5, 32, 64 ], name_conv2 )
  b_conv2 = makeBiasVariable( 64, name_conv2 )
  h_conv2 = tf.nn.relu( makeConv2d( h_pool1, W_conv2, name_conv2 ) + b_conv2 )

with tf.name_scope('pool2') as scope:
  h_pool2 = makeMaxPooling( h_conv2 )

with tf.name_scope('fully_conected') as scope:
  num    = 7 * 7 * 64
  W_flat = makeWeightVariable( [num, 1024], 'fully_conected' )
  b_flat = makeBiasVariable( 1024, 'fully_conected' )
  h_pool2_flat = tf.reshape( h_pool2, [-1, num] )
  h_fc   = tf.nn.relu( tf.matmul( h_pool2_flat, W_flat ) + b_flat )

with tf.name_scope('dropout1') as scope:
  keep_prob = tf.placeholder( tf.float32 )
  h_fc_drop = tf.nn.dropout( h_fc, rate=1-keep_prob )

with tf.name_scope('ouptut') as scope:
  W_output = makeWeightVariable( [1024, nums], 'ouptut' )
  b_output = makeBiasVariable( nums, 'ouptut' )
  y_conv   = tf.nn.softmax( tf.matmul( h_fc_drop, W_output ) + b_output )

y_ = tf.placeholder( tf.float32, shape=(None, nums), name='y_' )

with tf.name_scope( 'loss' ) as scope:
  cross_entropy = -tf.reduce_sum( y_*tf.log(y_conv) )

with tf.name_scope( 'sgd' ) as scope:
  optimizer = tf.train.AdamOptimizer()
  train     = optimizer.minimize( cross_entropy )

with tf.name_scope( 'predict' ) as scope:
  predict  = tf.equal( tf.arg_max(y_conv, 1), tf.arg_max(y_, 1) )
  accuracy = tf.reduce_mean( tf.cast( predict, tf.float32 ) )

def makeFeedDictParam( imgDatas,  labels,  prob ):
  return {x:imgDatas, y_:labels, keep_prob:prob}

TRAIN_COUNTS = 3000
ONE_TRAIN_AMT= 50
VERBOSE_TERM = 100
with tf.Session() as sess:
  sess.run( tf.global_variables_initializer() )
  test_feedDict = makeFeedDictParam( mnist.test.images, mnist.test.labels, 1.0 )
  for step in range(TRAIN_COUNTS):
    batch       = mnist.train.next_batch( ONE_TRAIN_AMT )
    train_fdp   = makeFeedDictParam( batch[0], batch[1], 0.5 )
    _, loss     = sess.run( [ train, cross_entropy ], feed_dict=train_fdp )
    if step % VERBOSE_TERM == 0:
      acc       = sess.run( accuracy, feed_dict=test_feedDict )
      print( 's=%4s, a=%20s, l=%20s' % (step, acc, loss) )
  acc = sess.run( accuracy, feed_dict=test_feedDict )
  print('-'*50)
  print('최종 결과')
  print( 's=%4s, a=%20s, l=%20s' % (step, acc, loss) )
  print('-'*50)