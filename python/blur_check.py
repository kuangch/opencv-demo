#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2018 Dilusense Inc. All Rights Reserved.


"""=======================================

    company : Dilusense
     author : Kuangch
       date : 2018/1/23

======================================="""

from imutils import paths
import argparse
import cv2


# 命令行参数
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', required=True, help="images directory paths")
ap.add_argument('-t', '--threshold', type=float, default=100.0, help="threshold of blur")
args = vars(ap.parse_args())

imgPaths = args['images']
threshold = args['threshold']


def verify_by_laplacian(image):
    """
    拉普拉斯算法求图片方差
    图片边缘越少（方差越小）越模糊
    :param image: 灰度图图片矩阵
    :return: 方差值
    """
    return cv2.Laplacian(image, cv2.CV_64F).var()


for imgPath in paths.list_images(imgPaths):
    print('img paths', imgPath)

    img = cv2.imread(imgPath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t = verify_by_laplacian(gray)

    cv2.putText(img,
                "{}: {:.2f}".format('blurry' if t < threshold else 'good', t),
                (20, 40),
                cv2.FONT_HERSHEY_COMPLEX,
                0.8,
                ((0, 0, 255) if t < threshold else (0, 255, 0)),
                1)

    cv2.imshow(imgPath, img)

    # 等待按键操作事件（可以监听按键进行后续操作，如保存图片等）
    key = cv2.waitKey(0)
    print(key)