#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2018 Dilusense Inc. All Rights Reserved.


"""=======================================

    company : Dilusense
     author : Kuangch
       date : 2018/1/23

======================================="""
import cv2 as cv

flags = [i for i in dir(cv) if i.startswith('COLOR_')]

for flag in flags:
    print(flag)