# import cv2
# import numpy as np
# from glob import glob
# import argparse
#
# from matplotlib import pyplot as plt
# import time
#
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from skimage.feature import hog
# from skimage.transform import resize
# from skimage.io import imread
# import os
# from sklearn.utils import shuffle
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import svm, datasets
#
# import os
# def train ():
#     train_path = args['train_path']
#     test_path = args['test_path']
#
#     images = None
#     trainImageCount = 0
#     train_labels = np.array([])
#     name_dict = {}
#     descriptor_list = []
#
#     images, trainImageCount = getFiles(train_path)
#     # extract SIFT Features from each image
#     label_count = 0
#     for word, imlist in images.items():
#         name_dict[str(label_count)] = word
#         print("Computing Features for ", word)
#         for im in imlist:
#             # cv2.imshow("im", im)
#             # cv2.waitKey()
#             train_labels = np.append(train_labels, label_count)
#             # kp, des = self.im_helper.features(im)
#             #  self.descriptor_list.append(des)
#             resizeimg = resize(im, (64, 64))
#             blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
#             fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
#                                 visualize=True
#                                 )
#          #   features = StandardScaler().fit_transform(fd.reshape(-1, 1))
#             descriptor_list.append(fd)
#         label_count += 1
#         X = descriptor_list
#         Y = train_labels
#         fe =[]
#
#     return X,Y
# def test():
#     test_path = args['test_path']
#
#     testImages, testImageCount = getFiles(test_path)
#
#    # predictions = []
#     test_img = []
#     label = []
#     label_count = 0
#     for word, imlist in testImages.items():
#         print("processing ", word)
#         for im in imlist:
#             # print imlist[0].shape, imlist[1].shape
#             print(im.shape)
#             resizeimg = resize(im, (64, 64))
#             blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
#             fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
#                                 visualize=True
#                                 )
#             test_img.append(fd)
#
#
#             label.append(label_count)
#         label_count += 1
#
#     return test_img,label,testImages
#
# def test1ormore():
#     test_pathormore = args['test_path1ormore']
#
#     testImages, testImageCount = getFiles(test_pathormore)
#
#    # predictions = []
#     test_img = []
#     label = []
#     label_count = 0
#     for word, imlist in testImages.items():
#         print("processing ", word)
#         for im in imlist:
#             # print imlist[0].shape, imlist[1].shape
#             print(im.shape)
#             resizeimg = resize(im, (64, 64))
#             blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
#             fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
#                                 visualize=True
#                                 )
#             test_img.append(fd)
#
#             label.append(label_count)
#         label_count += 1
#
#     return test_img,label,testImages
#
#
#
# def getFiles( path):
#
#         imlist = {}
#         count = 0
#         for each in os.listdir(path):
#             print(" #### Reading image category ", each, " ##### ")
#             imlist[each] = []
#             for imagefile in os.listdir(path + '/' + each):
#                 print("Reading file ", imagefile)
#                 im = cv2.imread(path + '/' + each + '/' + imagefile, 0)
#                 imlist[each].append(im)
#                 count += 1
#
#         return [imlist, count]
#
# parser = argparse.ArgumentParser(
#     description=" Bag of visual words example"
# )
# #
# # def predict_im(pl,imagee):
# #     predictions = []
# #     for  imlist in imagee.items(),pl:
# #
# #             predictions.append({
# #             'image': imlist,
# #
# #             'object_name': pl})
# #
# #     for each in predictions:
# #
# #         plt.imshow(cv2.cvtColor(each['image'], cv2.COLOR_GRAY2RGB))
# #         plt.title(each['object_name'])
# #         plt.show()
# #
#
# if __name__ == '__main__':
#
#     parser.add_argument('--train_path', default="ProductClassification\\train", action="store", dest="train_path")
#     parser.add_argument('--test_path', default="ProductClassification\\validation", action="store", dest="test_path")
#     parser.add_argument('--test_path1ormore', default="ProductClassification\\b1", action="store", dest="test_path1ormore")
#     args = vars(parser.parse_args())
#     print(args)
#     train_path = args['train_path']
#     test_path = args['test_path']
#
#
# #    test_img, label,im = test1ormore()
#     descriptor_list,train_labels=train()
#    # test_pathormore = args['test_path1ormore']
#     test_img, label,im = test()
#     #test_img, label = test()
#
#     start_time_fit_data = time.time()
#
#     lin_svc = svm.LinearSVC(C=1).fit(descriptor_list, train_labels)
#     time_lin_svc_fit_data = time.time() - start_time_fit_data
#     linear_acc_test = lin_svc.score(test_img, label) * 100
#     print('	Testing accuracy to Linear svm model', linear_acc_test)
#     linear_acc_train = lin_svc.score(descriptor_list, train_labels) * 100
#     print('training accuracy to Linear model', linear_acc_train)
#     start_time_predict_data = time.time()
#
#     p = lin_svc.predict(test_img)
#     time_lin_test_data = time.time() - start_time_predict_data
#     print(f"\n\033[92m time logistic to fit data: {time_lin_svc_fit_data}\033[0m")
#     print(f"\n\033[92m time logistic to fit data: {time_lin_test_data}\033[0m")
#     # # im_pr = []
#     # # im_pr.append(p)
#     # predict_im(p, im)
#
#     print(p)
#     ###########
#     start_time_fit1_data = time.time()
#     rbf_svc = svm.SVC(kernel='rbf', degree=5, C=1).fit(descriptor_list, train_labels)
#     time_rbf_svc_fit_data = time.time() - start_time_fit1_data
#     rpf_acc_test = rbf_svc.score(test_img, label)*100
#     print('	Testing accuracy to RPF model', rpf_acc_test)
#
#     rpf_acc_train = rbf_svc.score(descriptor_list, train_labels)*100
#     print('training accuracy to RPF model', rpf_acc_train)
#     start_time_predict1_data = time.time()
#     m=rbf_svc.predict(test_img)
#     time_rpf_test_data = time.time() - start_time_predict1_data
#     print(m)
#     print(f"\n\033[92m time logistic to fit data: {time_rbf_svc_fit_data}\033[0m")
#     print(f"\n\033[92m time logistic to fit data: {time_rpf_test_data}\033[0m")
#     # poly------------------------
#     start_time_fit2_data = time.time()
#     poly_svc = svm.SVC(kernel='poly', degree=3, C=1).fit(descriptor_list, train_labels)
#     time_poly_svc_fit_data = time.time() - start_time_fit2_data
#     poly_acc_test = poly_svc.score(test_img, label) * 100
#     print('	Testing accuracy to Polynomial model', poly_acc_test)
#     poly_acc_train = poly_svc.score(descriptor_list, train_labels) * 100
#     print('training accuracy to Polynomial model', poly_acc_train)
#     start_time_predoct2_data = time.time()
#     k=poly_svc.predict(test_img)
#     time_poly_predict_data = time.time() - start_time_predoct2_data
#     print(k)
#     print(f"\n\033[92m time logistic to fit data: {time_poly_svc_fit_data}\033[0m")
#     print(f"\n\033[92m time logistic to fit data: {time_poly_predict_data}\033[0m")
import cv2
import numpy as np
from glob import glob
import argparse

from matplotlib import pyplot as plt
import time

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from skimage.feature import hog
from skimage.transform import resize
from skimage.io import imread
import os
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

import os
def train ():
    train_path = args['train_path']
    test_path = args['test_path']

    images = None
    trainImageCount = 0
    train_labels = np.array([])
    name_dict = {}
    descriptor_list = []

    images, trainImageCount = getFiles(train_path)
    # extract SIFT Features from each image
    label_count = 0
    for word, imlist in images.items():
        name_dict[str(label_count)] = word
        print("Computing Features for ", word)
        for im in imlist:
            # cv2.imshow("im", im)
            # cv2.waitKey()
            train_labels = np.append(train_labels, label_count)
            # kp, des = self.im_helper.features(im)
            #  self.descriptor_list.append(des)
            resizeimg = resize(im, (64, 64))
            blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
            fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                                visualize=True
                                )
         #   features = StandardScaler().fit_transform(fd.reshape(-1, 1))
            descriptor_list.append(fd)
        label_count += 1
        X = descriptor_list
        Y = train_labels
        fe =[]

    return X,Y
def test():
    test_path = args['test_path']

    testImages, testImageCount = getFiles(test_path)

   # predictions = []
    test_img = []
    label = []
    label_count = 0
    for word, imlist in testImages.items():
        print("processing ", word)
        for im in imlist:
            # print imlist[0].shape, imlist[1].shape
            print(im.shape)
            resizeimg = resize(im, (64, 64))
            blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
            fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                                visualize=True
                                )
            test_img.append(fd)


            label.append(label_count)
        label_count += 1

    return test_img,label,testImages

def test1ormore():
    test_pathormore = args['test_path1ormore']

    testImages, testImageCount = getFiles(test_pathormore)

   # predictions = []
    test_img = []
    label = []
    label_count = 0
    for word, imlist in testImages.items():
        print("processing ", word)
        for im in imlist:
            # print imlist[0].shape, imlist[1].shape
            print(im.shape)
            resizeimg = resize(im, (64, 64))
            blurred_image = cv2.GaussianBlur(resizeimg, (5, 5), 0)
            fd, hog_image = hog(blurred_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                                visualize=True
                                )
            test_img.append(fd)

            label.append(label_count)
        label_count += 1

    return test_img,label,testImages



def getFiles(path):
    num_classes = 20
    imlist_train = []
    imlist_valid = []
    valid_labels = []
    for i in range(1, num_classes + 1):
        print(" #### Reading image category ", i, " ##### ")
        train_dir = "Data/Product Classification/" + str(i) + "/Train"
        validation_dir = "Data/Product Classification/" + str(i) + "/Validation"
        class_name = str(i)
        count = 0
        count_t=0
        count_v=0
        for filename in os.listdir(train_dir):
            if not filename.endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
                continue
            # if filename.endswith('.png'):
            img_path1 = os.path.join(train_dir, filename)
            imlist_train.append(img_path1)
            train_labels.append(class_name)
            count_t += 1

        for filename in os.listdir(validation_dir):
            if not filename.endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
                continue
            # if filename.endswith('.png'):
            img_path1 = os.path.join(validation_dir, filename)
            imlist_valid.append(img_path1)
            valid_labels.append(class_name)
            count_v += 1

    return [imlist_train, count]



parser = argparse.ArgumentParser(
    description=" Bag of visual words example"
)
#
# def predict_im(pl,imagee):
#     predictions = []
#     for  imlist in imagee.items(),pl:
#
#             predictions.append({
#             'image': imlist,
#
#             'object_name': pl})
#
#     for each in predictions:
#
#         plt.imshow(cv2.cvtColor(each['image'], cv2.COLOR_GRAY2RGB))
#         plt.title(each['object_name'])
#         plt.show()
#

if __name__ == '__main__':

    parser.add_argument('--train_path', default="Data/Product Classification/", action="store", dest="train_path")
    parser.add_argument('--test_path', default="Data/Product Classification", action="store", dest="test_path")
    parser.add_argument('--test_path1ormore', default="Data/Product Classification", action="store", dest="test_path1ormore")
    args = vars(parser.parse_args())
    print(args)
    train_path = args['train_path']
    test_path = args['test_path']


#    test_img, label,im = test1ormore()
    descriptor_list,train_labels=train()
   # test_pathormore = args['test_path1ormore']
    test_img, label,im = test()
    #test_img, label = test()

    start_time_fit_data = time.time()

    lin_svc = svm.LinearSVC(C=1).fit(descriptor_list, train_labels)
    time_lin_svc_fit_data = time.time() - start_time_fit_data
    linear_acc_test = lin_svc.score(test_img, label) * 100
    print('	Testing accuracy to Linear svm model', linear_acc_test)
    linear_acc_train = lin_svc.score(descriptor_list, train_labels) * 100
    print('training accuracy to Linear model', linear_acc_train)
    start_time_predict_data = time.time()

    p = lin_svc.predict(test_img)
    time_lin_test_data = time.time() - start_time_predict_data
    print(f"\n\033[92m time logistic to fit data: {time_lin_svc_fit_data}\033[0m")
    print(f"\n\033[92m time logistic to fit data: {time_lin_test_data}\033[0m")
    # # im_pr = []
    # # im_pr.append(p)
    # predict_im(p, im)

    print(p)
    ###########
    start_time_fit1_data = time.time()
    rbf_svc = svm.SVC(kernel='rbf', degree=5, C=1).fit(descriptor_list, train_labels)
    time_rbf_svc_fit_data = time.time() - start_time_fit1_data
    rpf_acc_test = rbf_svc.score(test_img, label)*100
    print('	Testing accuracy to RPF model', rpf_acc_test)

    rpf_acc_train = rbf_svc.score(descriptor_list, train_labels)*100
    print('training accuracy to RPF model', rpf_acc_train)
    start_time_predict1_data = time.time()
    m=rbf_svc.predict(test_img)
    time_rpf_test_data = time.time() - start_time_predict1_data
    print(m)
    print(f"\n\033[92m time logistic to fit data: {time_rbf_svc_fit_data}\033[0m")
    print(f"\n\033[92m time logistic to fit data: {time_rpf_test_data}\033[0m")
    # poly------------------------
    start_time_fit2_data = time.time()
    poly_svc = svm.SVC(kernel='poly', degree=3, C=1).fit(descriptor_list, train_labels)
    time_poly_svc_fit_data = time.time() - start_time_fit2_data
    poly_acc_test = poly_svc.score(test_img, label) * 100
    print('	Testing accuracy to Polynomial model', poly_acc_test)
    poly_acc_train = poly_svc.score(descriptor_list, train_labels) * 100
    print('training accuracy to Polynomial model', poly_acc_train)
    start_time_predoct2_data = time.time()
    k=poly_svc.predict(test_img)
    time_poly_predict_data = time.time() - start_time_predoct2_data
    print(k)
    print(f"\n\033[92m time logistic to fit data: {time_poly_svc_fit_data}\033[0m")
    print(f"\n\033[92m time logistic to fit data: {time_poly_predict_data}\033[0m")