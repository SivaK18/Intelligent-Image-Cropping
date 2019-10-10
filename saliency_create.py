# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:47:35 2019

@author: S.S.HARI
"""
import tensorflow as tf
import numpy as np
import os
from scipy import misc

g_mean = np.array(([126.88,120.24,112.19])).reshape([1,1,3])
saliency_folder = "./saliency_output"

def rgba2rgb(img):
	return img[:,:,:3]*np.expand_dims(img[:,:,3],2)

def saliency(folder,path):
			
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('./meta_graph/my-model.meta')
        saver.restore(sess,tf.train.latest_checkpoint('./salience_model'))
        image_batch = tf.get_collection('image_batch')[0]
        pred_mattes = tf.get_collection('mask')[0]
        if folder:
            rgb = misc.imread(os.path.join(folder,path))
        else:
            rgb = misc.imread(path)
        if rgb.shape[2]==4:
           rgb = rgba2rgb(rgb)
        origin_shape = rgb.shape[:2]
        rgb = np.expand_dims(misc.imresize(rgb.astype(np.uint8),[320,320,3],interp="nearest").astype(np.float32)-g_mean,0)
        feed_dict = {image_batch:rgb}
        pred_alpha = sess.run(pred_mattes,feed_dict = feed_dict)
        final_alpha = misc.imresize(np.squeeze(pred_alpha),origin_shape)
        misc.imsave(os.path.join(saliency_folder,path),final_alpha)


