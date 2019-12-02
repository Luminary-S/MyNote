# ros kinetic use roadmap 

## ros subscriber and publisher in python
refer: https://blog.csdn.net/qq_42145185/article/details/80404096
 
# add self-defined msg
refer: [创建ros msg 和 srv](https://blog.csdn.net/ab748998806/article/details/51188613 )
## msg
step：

   1.  在msg目录下使用msg文件语法定义一个msg
   2.  修改CmakeLists.txt，在find_package调用中，添加message_generation依赖
   3.  修改CmakeLists.txt，在catkin_message下添加message_runtime依赖
   4.  修改CmakeLists.txt，去掉add_message_files注释，添加我们自己定义的msg文件
   5.  修改CmakeLists.txt，去掉generate_messages()的注释

check：
rosmsg show beginner_tutorials/Num

ros 各种msg 类型可以用numpy 生成 `np.uint16(32)`

## srv
创建srv的流程同msg基本一致


# opencv 
为了避免使用ROSkinetic中的opencv3的库，就需要将其cv2.so删掉，为了以防万一，可以先将cv2.so移到其他地方

# python3.5 use ros
refer: [Ubuntu16.04下opencv2与ROSkinetic中自带opencv3不兼容问题总结](https://blog.csdn.net/qq_30460905/article/details/79845156)

To use ros in python 3.5 , you should add path :
```
/opt/ros/kinetic/lib/python2.7/dist-packages
```

# 界面辅助设置
1. 设置日志级别  refer:https://www.jianshu.com/p/8d23b4c12f6f
```
rqt_logger_level
```
2. 查看日志
```
rqt console
```
3. 查看image
```
rqt_image_view
```
4. 查看节点关系
```
rqt_graph
```
5. 修改参数服务器中参数的变量 rqt_reconfigure
```
rosrun rqt_reconfigure rqt_reconfigure
```
6. 显示数据流,画图
```
rqt_plot
```

# camera calibration
refer:https://blog.csdn.net/heyijia0327/article/details/43538695
需要三个工具:
* rqt_image_view
* usb_cam
* camera_calibration

标定cmd（0.03单位是m, 11*8 是标定板内点）
```
$ rosrun camera_calibration cameracalibrator.py --size 11x8 --square 0.006 image:=/usb_cam/image_raw camera:=/usb_cam
```

# ros 中 回调 并在qt gui中显示
1. 使用ros subscriber的视频信息，在callback中应该只使用msg的简单处理，不适合在callback中做复杂的处理，不然会影响callback调用的速度。这个在订阅ros image信息，并在自己设计的qtgui中显示非常重要。。。
2. qtgui中为显示大量的信息，需要使用多线程的方式。订阅的image显示，需要通过专门的QThread显示，在线程中处理简单的每帧，并发送一个signal，使用槽函数进行frame的显示。

# rospy 相关函数
refer : https://blog.csdn.net/qq_25678319/article/details/87938004

# ros logging
rospy 的logging 使用的是python的 logging 模块
refer: 
1. [python3_Logging模块详解](https://www.cnblogs.com/ranxf/p/7794240.html)
2. [ROS与C++入门教程-Logging(日志)](https://www.ncnynl.com/archives/201702/1299.html)

# ROS下同时接收多个话题并实现相机和雷达的数据融合
refer: 
1. https://blog.csdn.net/qq_29462849/article/details/88880699
2. https://blog.csdn.net/ttomchy/article/details/86179713
可以实现在视频流中显示雷达的激光线，无人车那个效果

# Rosbag 数据记录转换为mp4视频

1. 新建test.launch文件

新建test.launch文件，并写入如下内容：
```
<launch>
<node pkg="rosbag" type="play" name="rosbag" args="-d 2 home/rosbag/test.bag"/>
<node name="extract" pkg="image_view" type="extract_images" respawn="false" output="screen"   cwd="ROS_HOME">
  <remap from="image" to="image_raw"/>
</node>
</launch>
```
    第一个node标签末尾替换为自己的bag路径

2. 运行launch文件，生成jpg图片
```
roslaunch test.launch
```
此时，bag中的数据被分离成一组图片，存放在“.ros”文件夹中，现在将其转移到指定目录下：
```
mkdir testImg
mv ~/.ros/frame*.jpg testImg/
```
3. 将图片转换为视频
```
cd testImg
ffmpeg -r 15  -s 1280*800 -i frame%04d.jpg test.mp4
```
或
```
cd testImg
/* 生成yuv格式文件*/
jpeg2yuv -I p -f 15 -j frame%04d.jpg -b 1 > test.yuv
/* 将yuv格式文件转换为mp4格式*/
ffmpeg -i test.yuv test.mp4
```

# update warning when sudo update
please insert the lastest public-key into your system
```
http://wiki.ros.org/kinetic/Installation/Ubuntu
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

# catkin_make时提示from catkin_pkg.cli.find_pkg import main No module named 'catkin_pkg'

这个问题有多种可能性解决办法为：
1. solution for 1
```bash
pip install --user catkin_pkg
pip install --user rosdep dosinstall_generator wstool rosinstall six vcstools
pip install --user pydot
```
2. catkin_make 就不行，仔细看错误的提示，例如我的：
```CMake Error at CMakeLists.txt:20 (message):
  Search for 'catkin' in workspace failed (catkin_find_pkg catkin
  /home/sgl/catkin_new/src): Traceback (most recent call last):

    File "/home/sgl/.local/bin/catkin_find_pkg", line 5, in <module>
      from catkin_pkg.cli.find_pkg import main

  ModuleNotFoundError: No module named 'catkin_pkg'
```
关键是 file "/home/sgl/.local/bin/catkin_find_pkg", 去找这个文件，sudo 权限打开，看到里面的第一行是
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from catkin_pkg.cli.find_pkg import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```
这里用的是python3, 实际上ros用的是python2. 修改 这个地方为python2,就可以了。。