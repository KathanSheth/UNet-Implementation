import numpy as np

def load_train_data():
    train_images = np.load('train_images.npy')
    train_mask_images = np.load('train_mask_images.npy')
    return train_images,train_mask_images

def load_test_data():
    test_images = np.load('test_images.npy')
    test_id_images = np.load('test_id_images.npy')
    return test_images,test_id_images

