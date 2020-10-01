# 1. ros melodic use roadmap 
<!-- TOC -->

- [1. ros melodic use roadmap](#1-ros-melodic-use-roadmap)
  - [1. ros subscriber and publisher in python](#1-ros-subscriber-and-publisher-in-python)
- [2. add self-defined msg](#2-add-self-defined-msg)
  - [2.1. msg](#21-msg)
    - [2.1.1. define msg](#211-define-msg)
    - [2.1.2. 使用同一工作空间下另外包里面msg](#212-使用同一工作空间下另外包里面msg)
  - [2.2. srv](#22-srv)
- [3. opencv](#3-opencv)
- [4. python3.5 use ros](#4-python35-use-ros)
- [5. 界面辅助设置](#5-界面辅助设置)
- [6. camera calibration](#6-camera-calibration)
- [7. ros 中 回调 并在qt gui中显示](#7-ros-中-回调-并在qt-gui中显示)
- [8. rospy 相关函数](#8-rospy-相关函数)
- [9. ros logging](#9-ros-logging)
- [10. ROS下同时接收多个话题并实现相机和雷达的数据融合](#10-ros下同时接收多个话题并实现相机和雷达的数据融合)
- [11. Rosbag 数据记录转换为mp4视频](#11-rosbag-数据记录转换为mp4视频)
- [12. update warning when sudo update](#12-update-warning-when-sudo-update)
- [13. catkin_make时提示from catkin_pkg.cli.find_pkg import main No module named 'catkin_pkg'](#13-catkin_make时提示from-catkin_pkgclifind_pkg-import-main-no-module-named-catkin_pkg)
- [14. 使用动态参数服务器](#14-使用动态参数服务器)
    - [step](#step)
- [roslaunch](#roslaunch)

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
```
check：
rosmsg show beginner_tutorials/Num
```
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
rosparam set parameter_name value
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

# 14. 使用动态参数服务器
desription: 需要外部动态调整参数。例如控制中PID参数的调节，或者需要查看机器人在不同参数下的性能表现，此时外部参数的动态调节显得极其便利.
* refer: 
  1. [ROS使用动态参数](https://blog.csdn.net/weixin_42587961/article/details/86677829)
  2. [ROS WIKI:How to Write Your First .cfg File](http://wiki.ros.org/dynamic_reconfigure/Tutorials/HowToWriteYourFirstCfgFile)
### step
1. 安装dynamic_reconfigure软件包
   ```shell
   sudo apt-get install -y ros-kinetic-dynamic-reconfigure
   ```
2. 创建config file，可参考 `sonar_servo/config/dynamic.cfg`  
    ``` shell
    #in workspace
    mkdir config
    vim dynamic.cfg
    ```
3. 修改 cfg 文件的权限 ```sudo chmod 777 dynamic.cfg```
4. 编辑CMakeLists.txt, 加入`find_package` and `generate_dynamic_reconfigure_options`
   ```make
   #cmake顺序, 后面三个的node名称，必须直接手动输入不能用${}
   find_package
   include_directories
   generate_dynamic_reconfigure_options
   catkin_package
   add_executable
   add_dependecies
   target_link_libraies
   ```
5. 修改package.xml， 加入 
   ```xml
   <build_depend>dynamic_reconfigure</build_depend>
   <run_depend>dynamic_reconfigure</run_depend>
   ```
6. 编辑使用dynamic paramaters 的服务端 node, 就是你的业务逻辑，需要实时监测参数动态变化的node。rqt_configure相当于client，实时在rqt上面拖动的时候，你的业务node就会实时修改并在你的callback中执行相应的param的获取。
   ```cpp
    #include "ros/ros.h"
    
    #include <dynamic_reconfigure/server.h>
    #include <ROS_Test1/Test1_Config.h>
     
    void callback(ROS_Test1::Test1_Config &config, uint32_t level)
    {
    	ROS_INFO("Reconfigure Request: %d %f %s %s %d",
    		config.int_param,
    		config.double_param,
    		config.str_param.c_str(),
    		config.bool_param?"True":"False",
    		config.size);
    }
     
    int main(int argc, char **argv)
    {
    	ros::init(argc, argv, "node_e_dynamic_reconfigure");

    	dynamic_reconfigure::Server<ROS_Test1::Test1_Config> server;
    	dynamic_reconfigure::Server<ROS_Test1::Test1_Config>::CallbackType f;
    	f = boost::bind(&callback, _1, _2);
    	server.setCallback(f);

    	ros::spin();
    	return 0;
    }
   ```
7. 编译运行
   ```shell
    cd ~/catkin_ws
    catkin_make
    roscore
    新开终端执行：
    cd ~/catkin_ws
    source devel/setup.bash
    roslaunch packageName nodeName
    新开终端执行：
    rosrun rqt_reconfigure rqt_reconfigure
      ```

### note
1. 命名对应关系:
  * cfg 的 package 是你所在的package的名称，是为了根据这个cfg编译这个python文件generate 对应的头文件用的
  * exit 的第二个参数，就是你这个package的名字
  * add dependencies 第一个参数 就是这个node名称
2. gen.add 详解
   ```python
    gen.add(name, type, level, description, default, min, max)
    # example
    gen.add("int_param", int_t, 0, "int parameter", 1, 0, 10);
    gen.add("double_param", double_t, 0, "double parameter", .1, 0.0, 1.0);
    gen.add("bool_param", bool_t, 0, "bool parameter", True);
    gen.add("str_param", str_t, 0, "string parameter", "ROS_Test1");
   ```
    name: 参数的名称
    type: 参数类型
    level:一个传递给回调的位掩码
    description: 一个描述参数
    default: 节点启动的初始值
    min: 参数最小值
    max: 参数最大值
3. exit(gen)
    ```python
    exit(gen.generate(PACKAGE, "dynamic_tutorials", "Tutorials"))
    ```
    The last line simply tells the generator to generate the necessary files and exit the program. The second parameter is the name of a node this could run in (used to generate documentation only, **same as the node** you want to use this cfg), the third parameter is a name prefix the generated files will get (e.g. "\<name>Config.h" for c++, or "\<name>Config.py" for python. 

# roslaunch
refer: https://zhuanlan.zhihu.com/p/157526418