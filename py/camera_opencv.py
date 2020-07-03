#!/usr/bin/python
# -*- coding: utf-8 -*-
#author;sgl
#date: 20190805
import cv2 as cv2

capture = cv2.VideoCapture(2)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break