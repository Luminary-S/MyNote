Ubuntu 18.04 in Windows 10 two systems 
====
<!-- TOC -->

- [Ubuntu 18.04 in Windows 10 two systems](#ubuntu-1804-in-windows-10-two-systems)
- [1. Install](#1-install)
- [2. necessary software install](#2-necessary-software-install)
  - [2.1. **Terminator**](#21-terminator)
  - [2.2. **Sogou Pinyin**](#22-sogou-pinyin)
  - [2.3. **other Font install**](#23-other-font-install)
  - [2.4. **VS Code**](#24-vs-code)
  - [2.5. **Common Tools**](#25-common-tools)
  - [2.6. **ROS**](#26-ros)
  - [2.7. **Qt**](#27-qt)
    - [2.7.1. reference](#271-reference)
    - [2.7.2. download](#272-download)
    - [2.7.3. installation](#273-installation)
  - [2.8. **Opencv**](#28-opencv)
    - [2.8.1. reference](#281-reference)
    - [2.8.2. download](#282-download)
    - [2.8.3. install](#283-install)
    - [2.8.4. NOTE](#284-note)
    - [2.8.5. installation](#285-installation)
  - [2.9. **pdf reader**](#29-pdf-reader)
  - [2.10. **NVIDIA driver and CUDA and Cudnn, pycuda, tensorflow-gpu**](#210-nvidia-driver-and-cuda-and-cudnn-pycuda-tensorflow-gpu)
    - [2.10.1. Content](#2101-content)
    - [2.10.2. reference](#2102-reference)
    - [2.10.3. download](#2103-download)
    - [2.10.4. installation](#2104-installation)
      - [cuda and nvidia](#cuda-and-nvidia)
      - [cudnn](#cudnn)
      - [pycuda](#pycuda)
      - [tensorflow-gpu](#tensorflow-gpu)
- [3. unnecessary software install](#3-unnecessary-software-install)
  - [3.1. **Matlab 2018a**](#31-matlab-2018a)
  - [3.2. **PyQt5, python3 pycharm**](#32-pyqt5-python3-pycharm)
  - [3.3. **Pycharm**](#33-pycharm)
  - [3.4. **eric**](#34-eric)
  - [3.5. **java**](#35-java)
  - [3.6. **arduino**](#36-arduino)
  - [3.7. **Vrep**](#37-vrep)
  - [3.8. **SIMPACK**](#38-simpack)
  - [3.9. **latex in vs code and beamer**](#39-latex-in-vs-code-and-beamer)

<!-- /TOC -->


# 1. Install
1. check your computer as UEFI and Legacy 
2. in UEFI, pls choose UEFI as the first boot choice in the BIOS, BIOS can be entered through press btn when you start your computer. For Lenovo latest computers, press "enter" is ok, others may be "F12" or "F2";
3. plug in your Flash, and choose start with the "USB-HDD", something like that, just make sure you start the USB system, not the computer sytem;
4. step by step, just refer to  [ Ubuntu 16.04与Win10双系统双硬盘安装图解](https://blog.csdn.net/fesdgasdgasdg/article/details/54183577)
   - Be careful about the disk partition when you install
   - suggest partition plan: 
   
   | 目录  | 类型     | 文件类别   | 大小                          |
   | ----- | -------- | ---------- | ----------------------------- |
   | /     | 主分区   | EXT4       | 30GB                          |
   | /swap | 逻辑分区 | swap space | 4GB        2倍内存            |
   | /boot | 逻辑分区 | EXT4       | 300MB        至少200，我用1GB |
   | /home | 逻辑分区 | EXT4       | 剩余（at least 50GB）         |

    - install the bootloader in the /boot disk( carefully choose that )
5. 启动系统，在进入Grub界面时，按e键，进入编辑页面，在倒数第二行中，ro quiet splash后面添加nomodeset，这样进入系统后不会因为独显驱动问题而导致黑屏了或者界面卡死；在进入系统后，编辑文件/boot/grub/grub.cfg文件，搜索ro quiet splash关键词，同样追加nomodeset，然后 sudo update-grub, 这样不用每次启动系统前重复上述步骤了。

6. plug out U flash, try start with ubuntu and windows.

# 2. necessary software install

## 2.1. **Terminator**
1. a more flexible terminal for ubuntu
2. install with: ```sudo apt-get install terminator```
3. configuration setup:
    + it now can automatically change the default terminal as terminator, if not refer to [change terminator as default terminal](https://blog.csdn.net/weixin_40522162/article/details/80305611)
    + other settings, refer to [terminator settings](https://www.jianshu.com/p/cee2de32ca28)

## 2.2. **Sogou Pinyin**
refer: [ubuntu 18.04 LTS 安装搜狗输入法](https://www.jianshu.com/p/c936a8a2180e)  and  [Ubuntu14.04.2安装搜狗输入法](https://blog.csdn.net/q1302182594/article/details/47068641)
1. download: [sogou pinyin linux]( https://pinyin.sogou.com/linux/?r=pinyin )
2. install deb package: ```dpkg -i sougou****.deb ```
3. change to Chinese language in system setting if sogou pinyin is not activated

## 2.3. **other Font install**
1. pls refer to [ font install ]( https://blog.csdn.net/bitcarmanlee/article/details/79729634 )
2. just use the second ways, it is ok 
3. font download link, sample [monaco.ttf]: https://github.com/fangwentong/dotfiles/raw/master/ubuntu-gui/fonts/Monaco.ttf  

## 2.4. **VS Code**
1. you will have a simple and easy to use code IDE
2. download from the [vs code website](https://code.visualstudio.com/) 
3. always used plugin:
    + markdown all in one, markdown preview github style, markdown TOC
    + code runner, code spell checker, path Intellisense 
    + beautify, bracket pair colorizer2, indent rainbow, chinese language
    + pyqt, python,
    + latex workshop, latex snippets, latex-formatter
    + [other vs code plugins ]( https://www.jianshu.com/p/068db41b6dcc )
4. just use ```code ``` in terminal to start it
5. change theme: ctrl+shift+p --> theme

NOTE: if TOC not automatically changes line, set EOL to \r\n in setting
 
## 2.5. **Common Tools**
1. **git**: ```sudo apt-get install git```, git 的配置参看 git_roadmap.md
2. **vim**: ```sudo apt-get install vim```
3. **latest firefox**, download [firefox](https://www.mozilla.org/zh-CN/firefox/download/), create [shortcut](https://blog.csdn.net/qq_32166627/article/details/51108482); acc: ustc163; pwd, h; add-ons:
   1. lastpass
   2. grammarly
4. **mendeley**: ```sudo apt-get install mendeleydesktop ``` or download from website [mendeley](https://www.mendeley.com/repositories/ubuntu/stable/amd64/mendeleydesktop-latest)
5. **FoxitReader**
   1. download [FoxitReader](https://www.foxitsoftware.cn/pdf-reader/)
   2. install:
   ```bash
   tar xvzf FoxitReader2.1.0805_Server_x64_enu_Setup.run.tar.gz
   sudo chmod +x FoxitReader.enu.setup.2.1.0805\(r225432\).x64.run
   sudo ./FoxitReader.enu.setup.2.1.0805\(r225432\).x64.run
   # path : /opt/foxitsoftware/foxitreader
   ```
6. rtorrent torrent download: ```sudo apt install rtorrent```
7. Indicator Stickynotes (desktop stickynotes)
8. [Xmind8](https://www.xmind.cn/download/xmind8/) and [install crack tutorial](https://www.jianshu.com/p/9d93b1754549)
9. 词典goldendict, `sudo apt-get install goldendict`, add off-line dict files:[dict website](http://download.huzheng.org/zh_CN/); [reference](https://blog.csdn.net/clksjx/article/details/85052248); youdao dict online website: http://dict.youdao.com/search?q=%GDWORD%&ue=utf8&keyfrom=web.index

## 2.6. **ROS**
ubuntu 18.04 --> melodic; ubuntu 16.04--> kinetic
1. refer ros wiki page: [install kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) and [install blog](https://blog.csdn.net/softimite_zifeng/article/details/78632211)
2. install step:
   1. Setup your sources.list
    ```
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    ```
   2.  Set up your keys   
    ```
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    ```
   3. update package   
    ```
    sudo apt-get update
    ```
   4. Desktop-Full Install     
    ```bash
    sudo apt-get install ros-melodic-desktop-full
    ```
3. init step:
   1. Initialize rosdep 
   
    ```bash
    sudo rosdep init
    rosdep update
    ```
```
     关于ros安装过程中出现rosdep init ERROR: cannot download default sources list from:解决方法

1、打开terminal控制台，输入：sudo nano /etc/hosts 

      这个命令中的nano是文本编辑器，也可以用vim、gedit等打开；

2、在打开的文件末尾一行添加： 151.101.84.133 raw.githubusercontent.com

3、保存退出，在terminal中输入： sudo rosdep init

4、执行完输入：rosdep update即可

```
   2. Environment setup
   
    ```bash
    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ```
    3. Dependencies for building packages
   
    ```bash
    sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
    ```   
4. Create a ROS Workspace
   1. Create a ROS Workspace
   ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make
   ```
   2. source your new setup.*sh file
   ```bash
    source devel/setup.bash
   ```
   3. make sure ROS_PACKAGE_PATH environment variable includes the directory you're in
   ```bash
    echo $ROS_PACKAGE_PATH
    /home/youruser/catkin_ws/src:/opt/ros/kinetic/share
    方法如下：
    1、打开终端脚本～/.bashrc文件：$sudo gedit ~/.bashrc
    2、在文件末尾添加export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:/你的工作空间路径/src
   ```
5. Test
   1. 打开Termial，输入以下命令，初始化ROS环境：roscore
   2. 打开新的Termial，输入以下命令，弹出一个小乌龟窗口：rosrun turtlesim turtlesim_node
   3. 打开新的Termial，输入以下命令，可以在Termial中通过方向键控制小乌龟的移动：
   rosrun turtlesim turtle_teleop_key
   4. 打开新的Termial，输入以下命令，弹出新的窗口查看ROS节点信息：rosrun rqt_graph rqt_graph
6. compile, catkin_make
    ```bash
    sudo apt-get install ros-melodic-moveit ros-melodic-visp ros-melodic-urdfdom-py ros-melodic-ros-control ros-melodic-ros-type-introspection ros-melodic-rosserial ros-melodic-serial ros-melodic-joint-trajectory-controller ros-melodic-plotjuggler  ros-melodic-
    ```
    + [ros-industrial/universal_robot](https://github.com/ros-industrial/universal_robot/tree/melodic-devel)下载对应版本的universal_robot package
    + install  plotjuggler: sudo apt-get install ros-melodic-plotjuggler 
    + cfg 文件会 permission denied
        ```bash
        sudo chmod +777 /home/sgl/catkin_new/src/razor_imu_9dof-threetech/cfg/imu.cfg
        sudo chmod +777 /home/sgl/catkin_new/src/aruco_ros/aruco_ros/cfg/ArucoThreshold.cfg
        sudo chmod +x /home/sgl/catkin_new/src/universal_robot-melodic-devel/ur_driver/cfg/URDriver.cfg

        ```

## 2.7. **Qt**
### 2.7.1. reference
1. [install qt](https://wiki.qt.io/Install_Qt_5_on_Ubuntu) 
2. [install blog](https://blog.csdn.net/wuweifeng_2017/article/details/78322249) 
3. [configuration](https://www.helplib.com/ubuntu/article_170121) 
4. [install qt ros package](https://blog.csdn.net/u010925447/article/details/81702166)
### 2.7.2. download
1. link: [qt](http://download.qt.io/official_releases/qt/) 
2. acc: ustc 163; pwd:Sgl 
### 2.7.3. installation
1. just tar xvf file, and run
2. path configuration
   1. 在命令端口中输入命令：sudo vim /usr/lib/x86_64-linux-gnu/qt-default/qtchooser/default.conf  打开default.conf文件。
   2. 将第一行改为自己安装路径（这是我的安装路径/home/wwf/software/Qt5.8.0）下的bin目录的路径，第二行改为Qt5.8.0目录的路径
    default is:
    ```bash
        /usr/lib/x86_64-linux-gnu/qt4/bin
        /usr/lib/x86_64-linux-gnu           
    ```
    change to :
    ```bash
        /home/sgl/Qt5.12.2/5.12.2/gcc_64/bin
        /home/sgl/Qt5.12.2/5.12.2
    ```
3. default desktop icon change, pls refer to the qt official website

## 2.8. **Opencv**
NOTE: 下载版本一致的opencv 和 opencv_contrib
### 2.8.1. reference
1. [Ubuntu14.04 Opencv3.3.0 安装配置及测试](https://blog.csdn.net/lgh0824/article/details/78487234)
2. [ubuntu16.04安装opencv3.4.1教程](https://blog.csdn.net/cocoaqin/article/details/78163171)
3. [Install OpenCV 3.0 and Python 3.4+ on Ubuntu](https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)
4. [Ubuntu 16.04: How to install OpenCV](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)

### 2.8.2. download

1. [opencv3.4.6](https://opencv.org/releases/), download source file
2. [opencv_contrib-3.4.6](https://codeload.github.com/opencv/opencv_contrib/zip/3.4.6)
3. [opencv_contrib 下载驿站（百度云盘下载）](https://blog.csdn.net/weijifen000/article/details/87904707), all opencv_contrib version in baidu disk, since github is so slow!!!!

### 2.8.3. install
START:
1. create build folder:
    ```bash
    mkdir release; cd release
    ```
2. download open_contrib, set it in opencv_extra_modules_path:    
    ```bash
        cmake -D CMAKE_BUILD_TYPE=Release \
            -D CMAKE_INSTALL_PREFIX=/usr/local \
            -D OPENCV_EXTRA_MODULES_PATH=/home/sgl/opencv/opencv_contrib-3.4.6/modules/ \
            -D BUILD_EXAMPLES=ON \
            -D CUDA_GENERATION=Kepler ..      
    ```
3. make install
   ```bash
   sudo make install
   ```
4. revise ldconfig, refer to reference 1
5. change cv2.so , refer to referecne 3

### 2.8.4. NOTE
1. in-source builds are not allowed, ```rm CMakeCache.txt```   
2. [安装OpenCV时提示缺少boostdesc_bgm.i文件的问题解决方案（附带资源）](https://blog.csdn.net/AlexWang30/article/details/99612188)
3. [libcudnn.so.7 is not a symbolic link](https://www.jianshu.com/p/b308d3bbde8a)
4. [No module named load_config_py2问题解决](https://blog.csdn.net/XindaBlack/article/details/102613017),找到__init__.py的位置，修改43行，load py2的方式改的和load py3 一样即可

### 2.8.5. installation

1. check opencv version:
   
   ```bash
   pkg-config --modversion opencv
   ```
   in python :

   ```python
    import cv2
    cv2.__version__
   ```

## 2.9. **pdf reader**
1. recommend [master-pdf-editor](https://code-industry.net/public/master-pdf-editor-5.4.38-qt5-all.amd64.deb)(careful about qt version, active code: AZQWS_XEDC5_RFVT6-BY7G6-5DCSX), Foxcit Reade; also **okular** is simple and useful,apt-get can be obtain.
2. download [Foxcit Reader](https://www.foxitsoftware.cn/downloads/), automatically choose the version for your computer system.
3. download master pdf editor
   ```
   wget https://code-industry.net/public/master-pdf-editor-5.4.38-qt5.amd64.deb
   sudo dpkg -i master-pdf-editor-5.4.38-qt5.amd64.deb
   offline activation , copy ID and using [key-gen.exe](https://blog.csdn.net/qq_40623536/article/details/105601872) in windows
   UKH4RXVO2ZMCQEZL3A
Activation Code..: E18F11DDDD91759009536C6D4272680B013011EEL8PU0YU15V
   ```
4. chmod of run file and sudo ./*.run if you want to install it for all files


## 2.10. **NVIDIA driver and CUDA and Cudnn, pycuda, tensorflow-gpu**
>environment and target: \
>laptop: alienware 15R3 \
>CPU: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 8 cores \
>GPU: GP104M [GeForce GTX 1070 Mobile] \
>RAM:16GB
>ROM:250GB SSD
>CUDA: 10.2 \
>Cudnn: 7.6 \
>pycuda:2019.1.2 \
>tensorflow: 2.0.0b1 

### 2.10.1. Content
- [1. reference](#2102-reference)
- [2. download ](#2103-download )
- [3. cuda install ](#cuda-and-nvidia )
- [4. cudnn install ](#cudnn )
- [5. pycuda install ](#pycuda )
- [6. tensorflow-gpu](#tensorflow-gpu)

NOTE:  CUDA 10.2 自带 NVIDIA driver，所以不需要自己去安装nvidia 驱动，安装了还会有版本不和的问题， cuda runfile 后面带如：440_33 的就是nvidia driver的版本号

### 2.10.2. reference
1. [Ubuntu 14.04 上安装 CUDA 7.5/8.0 超详细教程](https://blog.csdn.net/masa_fish/article/details/51882183)
2. [Ubuntu 16.04 安装 CUDA10.1 （解决循环登陆的问题）](https://www.cnblogs.com/dinghongkai/p/11268976.html)
3. [cuda installation guide linux official](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile)
4. [cuda other source file for patch](https://docs.nvidia.com/drive/active/5.1.6.0L/nvvib_docs/DRIVE_OS_Linux_SDK_Development_Guide/baggage/nvscibuf_8h_source.html),可能你自己编译会少.h file, download here
5. [cudnn安装](https://www.jianshu.com/p/39a4b80e48b4)
6. [cudnn官网安装步骤](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#axzz4qYJp45J2)
7. [pycuda 之 安装与简单使用](https://blog.csdn.net/u014365862/article/details/85338619)
8. [Tensorflow2.0 GPU版本安装（CUDA10.0 + cuDNN7.5 + Tensorflow2.0 Alpha）](https://blog.csdn.net/qq_43673118/article/details/90140395)
9. [TensorFlow GPU (Ubuntu 18.04.2 + CUDA 10.0 + NVIDIA GeForce GTX 1050) ](https://hirooka.pro/machine-learning/tensorflow-gpu-ubuntu-cuda-nvidia-geforce/)
10. [tensoflow 安装官网page](https://tensorflow.google.cn/install/)
11. [tensorflow2.1.0-RC1 源码编译（CPU版本）](https://blog.csdn.net/qq_34347375/article/details/103547553), 按照tensorflow 官网说法，2.1.0是同时支持gpu和cpu的，如只需要cpu，加-cpu

### 2.10.3. download 
1. [cuda 10.2](https://developer.nvidia.com/cuda-downloads)， 选择runfile 
2. [cudnn](https://developer.nvidia.com/rdp/cudnn-download), 需要注册账号, use: cuhk， pwd:Sgl; three files: 
   1. cuDNN Runtime Library for Ubuntu18.04 (Deb) 
   2. cuDNN Developer Library for Ubuntu18.04 (Deb) 
   3. cuDNN Code Samples and User Guide for Ubuntu18.04 (Deb) 
3. [pycuda 官网](https://www.lfd.uci.edu/~gohlke/pythonlibs/?cm_mc_uid=08085305845514542921829&cm_mc_sid_50200000=1456395916#pycuda)

### 2.10.4. installation
#### cuda and nvidia
* uninstall method: 
> sudo /usr/local/cuda-10.2/bin/cuda-uninstaller\
> sudo /usr/bin/nvidia-uninstall
* remove
>To remove CUDA Toolkit:\
> sudo apt-get --purge remove "*cublas*" "cuda*"\
>To remove NVIDIA Drivers:\
> sudo apt-get --purge remove "*nvidia*"

1.  检查自己的电脑环境是否具备安装CUDA的条件

    ```bash
    #会显示自己的NVIDIA GPU版本信息,check its cuda version
    lspci | grep -i nvidia 

    # check uour ubuntu version to check its cuda version
    uname -m && cat /etc/*release 

    #可以查看自己的gcc版本信息
    gcc –version 
    # if no
    sudo apt-get install gcc

    #可以查看自己的kernel版本信息
    uname –r

    #安装对应kernel版本的kernel header和package development
    sudo apt-get install linux-headers-$(uname -r)
    ```
2. dowload runfile, refer to [download](#12172-download)
3. runfile安装cuda
    ```bash
    #有输出则代表nouveau正在加载,需禁用, nouveau是ubuntu自带的开源的显卡驱动，不适合
    lsmod | grep nouveau

    #禁用 nouveau
    sudo vim /etc/modprobe.d/blacklist-nouveau.conf

    #add in file:
    blacklist nouveau
    options nouveau modeset=0

    #运行禁用
    sudo update-initramfs –u

    #检查是否禁用成功,无输出代表成功
    lsmod | grep nouveau 

    reboot

    #到达登录界面时，alt+ctrl+f1，进入tty1, text mode，登录账户

    #使用lightdm 关闭图形化界面
    sudo apt install lightdm
    sudo service lightdm stop

    cd ~/Downloads
    sudo chmod +x cuda***.run
    # install without install opengl package, opengl will makes the desktop restart in loops 
    sudo ./cuda***.run --no-opengl-libs

    #出现安装框的选择是(遇到提示是否安装openGL ，选择no（如果你的电脑跟我一样是双显，且主显是非NVIDIA的GPU需要选择no，否则可以yes）):
    accept
    options--> nvidia driver --> choose *, choose 1. no opengl; 2.not install drms (update management); 3.update X configure
    其他都选择yes或者默认

    # 重新启动图形化界面
    sudo service lightdm start

    Alt + ctrl +F7，返回到图形化登录界面，输入密码登录;
    如果能够成功登录，则表示不会遇到循环登录的问题，基本说明CUDA的安装成功了。

    #检查Device Node Verification
    检查路径/dev下 有无存在名为nvidia*（以nvidia开头）的多个文件(device files)
    如果没有的话，可以参考官方文档里的指导步骤，进行添加。

    #设置环境变量,永久添加， profile
    sudo gedit /etc/profile
    #add in file:
    export PATH=/usr/local/cuda-10.2/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64
    #同样在.bashrc也可以

    reboot

    #检查上述的环境变量是否设置成功
    env
    ```
4. 安装完毕后的检查工作
    ```bash
    #检查 NVIDIA Driver是否安装成功
    cat /proc/driver/nvidia/version

    #检查 CUDA Toolkit是否安装成功
    nvcc –V
    # 可以一次性查看
    nvidia-smi

    #编译cuda提供的例子
    cd ~/NVIDIA_CUDA-10.2_Samples
    # -k means keep going when error, some .h file may miss
    make -k
    cd ~/NVIDIA_CUDA-7.5_Samples/bin/x86_64/linux/release
    ./deviceQuery
    # if no error, congrats!!!
    ```
* 其他：检查 Device Node Verification（好像没什么影响）
    ```bash
    ls /dev/nvidia*

    #若显示类似 No such file or directory等信息，则进行如下操作

    sudo vim /etc/rc.local

    #把下面的文本复制到 exit 0 之前，保存退出
    
    #!/bin/sh
    /sbin/modprobe nvidia
    if [ "$?" -eq 0 ]; then
    　　# Count the number of NVIDIA controllers found.
    　　NVDEVS=`lspci | grep -i NVIDIA`
    　　N3D=`echo "$NVDEVS" | grep "3D controller" | wc -l`
    　　NVGA=`echo "$NVDEVS" | grep "VGA compatible controller" | wc -l`
    　　N=`expr $N3D + $NVGA - 1`
    　　for i in `seq 0 $N`; do
    　　　　mknod -m 666 /dev/nvidia$i c 195 $i
    　　done
    　　mknod -m 666 /dev/nvidiactl c 195 255
    else
    　　exit 1
    fi
    /sbin/modprobe nvidia-uvm
    if [ "$?" -eq 0 ]; then
    　　# Find out the major device number used by the nvidia-uvm driver
    　　D=`grep nvidia-uvm /proc/devices | awk '{print $1}'`
    　　mknod -m 666 /dev/nvidia-uvm c $D 0
    else
    　　exit 1
    fi

    #重启后，再次输入以下命令，此时应该会出现 
    ls /dev/nvidia*
    /dev/nvidia0   /dev/nvidiactl    /dev/nvidia-uvm，说明安装成功
   
    ```


#### cudnn 
* 如果deb 使用dpkg -i 出现 .deb not a deb file error, 可以直接对deb文件在新得利软件管理中心安装，就是右键deb文件后--> open with software install 
* 这里使用的是官网写的ubuntu的第二种deb安装方式，不需要拷贝cudnn.h 文件到cuda目录的，所以没办法使用 cat cudnn.h 的方式检查cudnn的版本,但是可以通过
  
1. 安装(both ok)
    1. Installing From A Tar File
    ```bash
    #Navigate to your <cudnnpath> directory containing the cuDNN Tar file.    Unzip the cuDNN package.
    $ tar -xzvf cudnn-10.2-linux-x64-v7.6.5.32.tgz

    #Copy the following files into the CUDA Toolkit directory, and change the file permissions.
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
    # add following in bashrc
    vim ~/.bashrc
    export CUDNN_PATH="/usr/local/cuda-10.2/lib64/libcudnn.so"
    ```

    2. Installing From A Debian File
    ```bash
    #Navigate to your <cudnnpath> directory containing cuDNN Debian file.    Install the runtime library, for example:
    sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb

    #Install the developer library, for example:
    sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.2_amd64.deb

    #Install the code samples and the cuDNN Library User Guide, for example:
    sudo dpkg -i libcudnn7-doc_7.6.5.32-1+cuda10.2_amd64.deb
    ```

2. 测试   
    ```bash
    #拷贝文件到环境配置的Home路径下 
    cp -r /usr/src/cudnn_samples_v7/ ~
    #切换路径 
    cd ~/cudnn_samples_v7/mnistCUDNN 
    #编译测试文件 
    make clean && make 
    #运行示例，如果成功则证明安装成功。 
    ./mnistCUDNN 
    ```
    
#### pycuda
* 查看pycuda的对应版本去[pycuda 官网](https://www.lfd.uci.edu/~gohlke/pythonlibs/?cm_mc_uid=08085305845514542921829&cm_mc_sid_50200000=1456395916#pycuda)；
    ```bash
    #查看CUDA版本, 2020-01-08, latest 10.2
    cat /usr/local/cuda/version.txt

    #查看cudnn版本,7.6：
    cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2 

    #安装
    sudo pip install pycuda
    sudo pip3 install pycuda==2019.1.2
    ```
#### tensorflow-gpu
this method install the version can be checked by pip3 search tensorflow-gpu, however, may not suits the cuda version.
* pre install:
  ```bash
  sudo pip3 install wheel
  ```
* 最好是建立一个python 的虚拟环境后安装，建立虚拟环境
    ```bash
    sudo pip3 install python3-venv

    mkdir ~/python_env; cd ~/python_env
    #create python env 
    python3 -m venv tf_env

    cd tf_env
    source bin/activate

    which python;which pip;pip -V
    ```
    Install:
    ```bash
    pip search tensorflow-gpu
    pip install tensorflow-gpu==2.0.0b1
    
    ```
* TF 源码安装需要 bazel 和 TF source code
  1. bazel 安装参考： [bazel 官网](https://docs.bazel.build/versions/master/install-ubuntu.html)
  2. [TF source 2.1.0-rc1 code](https://codeload.github.com/tensorflow/tensorflow/tar.gz/v2.1.0-rc1), and [tf github](https://github.com/tensorflow/tensorflow)

# 3. unnecessary software install
## 3.1. **Matlab 2018a** 
refer: 
1. [linux安装MATLAB R2018a步骤](https://blog.csdn.net/m0_37775034/article/details/80876362)
2. [Ubuntu 18.04 环境下安装 Matlab2018](https://www.cnblogs.com/yhjoker/p/11464679.html)

START
1. mount iso
   ```bash
   cd /mnt
   sudo chmod 755 mnt
   sudo mkdir iso
   sudo mount -t auto -o loop R2018a_glnxa64_dvd1.iso /mnt/iso
   ```
2. sudo /mnt/iso/install  开始安装
3. I have the File Installation Key for my license,输入:09806-07443-53955-64350-21751-41297
4. 安装完成后，将crack里面的R2018a/bin 文件复制替换到安装目录下/usr/local/MATLAB/R2018a/：sudo cp -rvf R2018a/bin /usr/local/MATLAB/R2018a/
5. 复制破解文件Crack中license_standalone.lic到安装目录中
    ```bash
    cd ~/Crack
    sudo cp license_standalone.lic /usr/local/MATLAB/R2018a/licenses
    ```
6. tools for matlab icon: sudo apt install matlab-support
7.  取消挂载,删除文件
    ```bash
        sudo umount /mnt/iso
        cd /mnt
        sudo rmdir iso
    ```

## 3.2. **PyQt5, python3 pycharm**
1. refer : https://www.jianshu.com/p/094928ac0b73
2. python doc 查看所有的 安装包
   ```bash
   python -m pydoc -p 1234
   pydoc server ready at http://localhost:1234/
   ```

## 3.3. **Pycharm**
1. the most common used Python IDE
2. install refer: (https://www.itread01.com/content/1544656170.html)
3. download: [pycharm](https://www.jetbrains.com/pycharm/), you can download community version, or professional version
4. activate method:
    1. revise the computer host file, to shield the access to Jetbrain website, so that no check will be made by Jetbrain.
        + ```sudo gedit /etc/hosts```
        + add:  ```0.0.0.0 account.jetbrains.com``` and ```0.0.0.0 www.jetbrains.com```
    2. add crack patch in python bin directory
        + download crack [JetbrainsCrack-2.6.10-release-enc.jar](https://pan.baidu.com/s/1w2hx5GAbQ7d7fVQ0HJdVZA)
        + move it in to : ``` /package path/python-***/bin```
    3. install 
        + ```sh ./pycharm.sh```  to start
        + in the active window, choose the second one（activation code), then browser to http://idea.lanyus.com/, get the activation code from the website, copy the code to the box.

## 3.4. **eric**
1. eric is a simple and perfect GUI develop IDE for PyQt and also it can be configured to develop other GUI, here only consider PyQt
2. refer [eric6 install](https://blog.csdn.net/suxiang198/article/details/52042526)
3. download page, [eric6.19](https://sourceforge.net/projects/eric-ide/)
4. pls install: QT, PyQt5, Python3+, SIP, QScintilla
    ```bash
    pip3 install PyQt5
    pip3 install sip
    pip3 install qscintilla
    python3 packagefile/eric/install.py
    ```
5. [eric settings](https://blog.csdn.net/mengyoufengyu/article/details/50927875)

## 3.5. **java**
1. download page, [java jdk](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
2. install refer: [install jdk8](https://blog.csdn.net/u012707739/article/details/78489833), use last method

## 3.6. **arduino**
1. download page, [arduino](https://www.arduino.cc/en/main/software?setlang=cn)
2. install refer: [install arduino](https://linux.cn/article-6778-1.html)

## 3.7. **Vrep**
1. download page, [vrep](http://coppeliarobotics.com/ubuntuVersions.html)
2. install refer: [install vrep](https://www.cnblogs.com/21207-iHome/p/7855947.html)
3. [python vrep](https://github.com/Troxid/vrep-api-python)

## 3.8. **SIMPACK**
1. download ：http://www.3322.cc/soft/35934.html
2. install: [SIMPACK2018 64](https://blog.csdn.net/xiaojuzitou/article/details/83144788)

## 3.9. **latex in vs code and beamer**
1. 安装Latex环境
```
# 安装latex
sudo apt-get install texlive-latex-base
# 安装中文环境
sudo apt-get install latex-cjk-all
# 安装额外包
sudo apt-get install texlive-latex-extra

# 安装图形界面texmaker
# sudo apt-get install texmaker

# 安装xelatex
sudo apt-get install texlive-xetex

# 安装publisher
sudo apt-get install texlive-publishers

# install beamer.cls
sudo apt install texlive-latex-recommended
```
2. 下载vscode
    [官网下载](https://code.visualstudio.com/​code.visualstudio.com)
3. 安装vscode
```
sudo dpkg -i <vs code名字>.deb
```
4. 安装插件Latex Workshop

打开VS code，在插件栏搜索latex workshop,点击install


4. 配置插件,打开setting.json，搜索latex-workshop.latex.recipes
点击Edit in settings.json,写入下列行：
```
"latex-workshop.latex.recipes": [
        {
            "name": "xelatex",
        "tools": [
          "xelatex"
        ]
        },
        {
        "name": "xelatex->bibtex->exlatex*2",
        "tools": [
          "xelatex",
          "bibtex",
          "xelatex",
          "xelatex"
        ]
      }],
 
    "latex-workshop.latex.tools":[
        {
            "name":"xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        }, {
            "name":"bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
```

