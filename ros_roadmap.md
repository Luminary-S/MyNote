# 1. ros kinetic use roadmap 
<!-- TOC -->

- [1. ros kinetic use roadmap](#1-ros-kinetic-use-roadmap)
  - [1. ros subscriber and publisher in python](#1-ros-subscriber-and-publisher-in-python)
- [2. add self-defined msg](#2-add-self-defined-msg)
  - [2.1. msg](#21-msg)
    - [2.1.1. define msg](#211-define-msg)
    - [2.1.2. 使用同一工作空间下另外包里面msg](#212-%e4%bd%bf%e7%94%a8%e5%90%8c%e4%b8%80%e5%b7%a5%e4%bd%9c%e7%a9%ba%e9%97%b4%e4%b8%8b%e5%8f%a6%e5%a4%96%e5%8c%85%e9%87%8c%e9%9d%a2msg)
  - [2.2. srv](#22-srv)
- [3. opencv](#3-opencv)
- [4. python3.5 use ros](#4-python35-use-ros)
- [5. 界面辅助设置](#5-%e7%95%8c%e9%9d%a2%e8%be%85%e5%8a%a9%e8%ae%be%e7%bd%ae)
- [6. camera calibration](#6-camera-calibration)
- [7. ros 中 回调 并在qt gui中显示](#7-ros-%e4%b8%ad-%e5%9b%9e%e8%b0%83-%e5%b9%b6%e5%9c%a8qt-gui%e4%b8%ad%e6%98%be%e7%a4%ba)
- [8. rospy 相关函数](#8-rospy-%e7%9b%b8%e5%85%b3%e5%87%bd%e6%95%b0)
- [9. ros logging](#9-ros-logging)
- [10. ROS下同时接收多个话题并实现相机和雷达的数据融合](#10-ros%e4%b8%8b%e5%90%8c%e6%97%b6%e6%8e%a5%e6%94%b6%e5%a4%9a%e4%b8%aa%e8%af%9d%e9%a2%98%e5%b9%b6%e5%ae%9e%e7%8e%b0%e7%9b%b8%e6%9c%ba%e5%92%8c%e9%9b%b7%e8%be%be%e7%9a%84%e6%95%b0%e6%8d%ae%e8%9e%8d%e5%90%88)
- [11. Rosbag 数据记录转换为mp4视频](#11-rosbag-%e6%95%b0%e6%8d%ae%e8%ae%b0%e5%bd%95%e8%bd%ac%e6%8d%a2%e4%b8%bamp4%e8%a7%86%e9%a2%91)
- [12. update warning when sudo update](#12-update-warning-when-sudo-update)
- [13. catkin_make时提示from catkin_pkg.cli.find_pkg import main No module named 'catkin_pkg'](#13-catkinmake%e6%97%b6%e6%8f%90%e7%a4%bafrom-catkinpkgclifindpkg-import-main-no-module-named-catkinpkg)

<!-- /TOC -->

## 1. ros subscriber and publisher in python
refer: https://blog.csdn.net/qq_42145185/article/details/80404096
 
# 2. add self-defined msg
refer: [创建ros msg 和 srv](https://blog.csdn.net/ab748998806/article/details/51188613 )
## 2.1. msg

### 2.1.1. define msg
step：

   1.  在msg目录下使用msg文件语法定义一个msg
   2.  修改CmakeLists.txt，在find_package调用中，添加message_generation依赖
   3.  修改CmakeLists.txt，在catkin_message下添加message_runtime依赖
   4.  修改CmakeLists.txt，去掉add_message_files注释，添加我们自己定义的msg文件
   5.  修改CmakeLists.txt，去掉generate_messages()的注释
   6.  在 package.xml 中 添加 （下面 exec_depend 有的也写成run_depend）
   ```
   <build_depend>message_generation</build_depend>
   <exec_depend>message_runtime</exec_depend>
  ```  

check：
rosmsg show beginner_tutorials/Num

ros 各种msg 类型可以用numpy 生成 `np.uint16(32)`

### 2.1.2. 使用同一工作空间下另外包里面msg

step:
1. 修改CmakeLists.txt，在find_package调用中，添加相应的 包的名称 如 demo_singlercr
2. 在 package.xml 中 添加
   ```
   <build_depend>demo_singlercr</build_depend>
   <exec_depend>demo_singlercr</exec_depend>
  ```

## 2.2. srv
创建srv的流程同msg基本一致


# 3. opencv 
为了避免使用ROSkinetic中的opencv3的库，就需要将其cv2.so删掉，为了以防万一，可以先将cv2.so移到其他地方

# 4. python3.5 use ros
refer: [Ubuntu16.04下opencv2与ROSkinetic中自带opencv3不兼容问题总结](https://blog.csdn.net/qq_30460905/article/details/79845156)

To use ros in python 3.5 , you should add path :
```
/opt/ros/kinetic/lib/python2.7/dist-packages
```

# 5. 界面辅助设置
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

# 6. camera calibration
refer:https://blog.csdn.net/heyijia0327/article/details/43538695
需要三个工具:
* rqt_image_view
* usb_cam
* camera_calibration

标定cmd（0.03单位是m, 11*8 是标定板内点）
```
$ rosrun camera_calibration cameracalibrator.py --size 11x8 --square 0.006 image:=/usb_cam/image_raw camera:=/usb_cam
```

# 7. ros 中 回调 并在qt gui中显示
1. 使用ros subscriber的视频信息，在callback中应该只使用msg的简单处理，不适合在callback中做复杂的处理，不然会影响callback调用的速度。这个在订阅ros image信息，并在自己设计的qtgui中显示非常重要。。。
2. qtgui中为显示大量的信息，需要使用多线程的方式。订阅的image显示，需要通过专门的QThread显示，在线程中处理简单的每帧，并发送一个signal，使用槽函数进行frame的显示。

# 8. rospy 相关函数
refer : https://blog.csdn.net/qq_25678319/article/details/87938004

# 9. ros logging
rospy 的logging 使用的是python的 logging 模块
refer: 
1. [python3_Logging模块详解](https://www.cnblogs.com/ranxf/p/7794240.html)
2. [ROS与C++入门教程-Logging(日志)](https://www.ncnynl.com/archives/201702/1299.html)

# 10. ROS下同时接收多个话题并实现相机和雷达的数据融合
refer: 
1. https://blog.csdn.net/qq_29462849/article/details/88880699
2. https://blog.csdn.net/ttomchy/article/details/86179713
可以实现在视频流中显示雷达的激光线，无人车那个效果

# 11. Rosbag 数据记录转换为mp4视频

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

# 12. update warning when sudo update
please insert the lastest public-key into your system
```
http://wiki.ros.org/kinetic/Installation/Ubuntu
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

# 13. catkin_make时提示from catkin_pkg.cli.find_pkg import main No module named 'catkin_pkg'

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