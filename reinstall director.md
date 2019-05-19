# 1. Ubuntu 16.04 and windowns 10 two systems 
<!-- TOC -->

- [1. Ubuntu 16.04 and windowns 10 two systems](#1-ubuntu-1604-and-windowns-10-two-systems)
  - [1.1. Install](#11-install)
  - [1.2. software install](#12-software-install)
    - [1.2.1. **Terminator**](#121-terminator)
    - [1.2.2. **Sogou Pinyin**](#122-sogou-pinyin)
    - [1.2.3. **other Font install**](#123-other-font-install)
    - [1.2.4. **VS Code**](#124-vs-code)
    - [1.2.5. **Common Tools**](#125-common-tools)
    - [1.2.6. **Pycharm**](#126-pycharm)
    - [1.2.7. **ROS**](#127-ros)
    - [1.2.8. **Qt**](#128-qt)
    - [1.2.9. **PyQt5, python3 pycharm**](#129-pyqt5-python3-pycharm)
    - [1.2.10. **Opencv**](#1210-opencv)
    - [1.2.11. **pdf reader**](#1211-pdf-reader)
    - [1.2.12. **eric**](#1212-eric)
    - [1.2.13. **java**](#1213-java)
    - [1.2.14. **arduino**](#1214-arduino)
    - [1.2.15. **Vrep**](#1215-vrep)

<!-- /TOC -->
## 1.1. Install
1. check your computer as UEFI and Legacy 
2. in UEFI, pls choose UEFI as the first boot choice in the BIOS, BIOS can be entered through press btn when you start your computer. For Lenovo latest computers, press "enter" is ok, others may be "F12" or "F2";
3. plug in your Flash, and choose start with the "USB-HDD", something like that, just make sure you start the USB system, not the computer sytem;
4. step by step, just refer to  [ Ubuntu 16.04与Win10双系统双硬盘安装图解](https://blog.csdn.net/fesdgasdgasdg/article/details/54183577)
   - Be careful about the disk partition when you install
   - suggest partition plan: 
   
   |目录| 类型|文件类别|大小|
   | ----- | -------- | ---------- | --------------------- |
   | /     | 主分区   | EXT4       | 30GB                  |
   | /swap | 逻辑分区 | swap space | 4GB                   |
   | /boot | 逻辑分区 | EXT4       | 300MB                 |
   | /home | 逻辑分区 | EXT4       | 剩余（at least 50GB） |

    - install the bootloader in the /boot disk( carefully choose that )
5. plug out U flash, try start with ubuntu and windows.

## 1.2. software install

### 1.2.1. **Terminator**
1. a more flexible terminal for ubuntu
2. install with: ```sudo apt-get install terminator```
3. configuration setup:
    + it now can automatically change the default terminal as terminator, if not refer to [change terminator as default terminal](https://blog.csdn.net/weixin_40522162/article/details/80305611)
    + other settings, refer to [terminator settings](https://www.jianshu.com/p/cee2de32ca28)

### 1.2.2. **Sogou Pinyin**
1. download: [sogou pinyin linux]( https://pinyin.sogou.com/linux/?r=pinyin )
2. install deb package: ```dpkg -i sougou****.deb ```

### 1.2.3. **other Font install**
1. pls refer to [ font install ]( https://blog.csdn.net/bitcarmanlee/article/details/79729634 )
2. just use the second ways, it is ok 
3. font download link, sample [monaco.ttf]: https://github.com/fangwentong/dotfiles/raw/master/ubuntu-gui/fonts/Monaco.ttf  

### 1.2.4. **VS Code**
1. you will have a simple and easy to use code IDE
2. download from the [vs code website](https://code.visualstudio.com/) 
3. always used plugin:
    + Chinese
    + markdown all in one, and markdown pdf
    + beautify, code spellcheck
    + others, refer to [vs code plugins ]( https://www.jianshu.com/p/068db41b6dcc )
4. just use ```code ``` in terminal to start it
 
### 1.2.5. **Common Tools**
1. **git**: ```sudo apt-get install git```
2. **vim**: ```sudo apt-get install vim```
3. **latest firefox**, download [firefox](https://www.mozilla.org/zh-CN/firefox/download/), create [shortcut](https://blog.csdn.net/qq_32166627/article/details/51108482)
4. **mendeley**: ```sudo apt-get install mendeleydesktop ``` or download from website [mendeley](https://www.mendeley.com/repositories/ubuntu/stable/amd64/mendeleydesktop-latest)

### 1.2.6. **Pycharm**
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

### 1.2.7. **ROS**
1. refer ros wiki page: [install kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) and [install blog](https://blog.csdn.net/softimite_zifeng/article/details/78632211)
2. install step:
   1. Setup your sources.list
    ```
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    ```
   2.  Set up your keys   
    ```
    sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    ```
   3. update package   
    ```
    sudo apt-get update
    ```
   4. Desktop-Full Install     
    ```bash
    sudo apt-get install ros-kinetic-desktop-full
    ```
3. init step:
   1. Initialize rosdep 
   
    ```bash
    sudo rosdep init
    rosdep update
    ```
   2. Environment setup
   
    ```bash
    echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ```
    3. Dependencies for building packages
   
    ```bash
    sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
    ```   
4. Create a ROS Workspace
   1. Create a ROS Workspace
   ```bash
    $ mkdir -p ~/catkin_ws/src
    $ cd ~/catkin_ws/
    $ catkin_make
   ```
   2. source your new setup.*sh file
   ```bash
    source devel/setup.bash
   ```
   3. make sure ROS_PACKAGE_PATH environment variable includes the directory you're in
   ```bash
    $ echo $ROS_PACKAGE_PATH
    /home/youruser/catkin_ws/src:/opt/ros/kinetic/share
   ```
5. Test
   1) 打开Termial，输入以下命令，初始化ROS环境：roscore
   2) 打开新的Termial，输入以下命令，弹出一个小乌龟窗口：rosrun turtlesim turtlesim_node
   3) 打开新的Termial，输入以下命令，可以在Termial中通过方向键控制小乌龟的移动：
   rosrun turtlesim turtle_teleop_key
   1) 打开新的Termial，输入以下命令，弹出新的窗口查看ROS节点信息：rosrun rqt_graph rqt_graph
6. compile, catkin_make
    + sudo apt-get install ros-kinetic-moveit ros-kinetic-visp ros-kinetic-urdfdom-py ros-kinetic-ros-control ros-kinetic-ros-type-introspection

### 1.2.8. **Qt**
1. refer: qt official website [install qt](https://wiki.qt.io/Install_Qt_5_on_Ubuntu) and [install blog](https://blog.csdn.net/wuweifeng_2017/article/details/78322249) and [configuration](https://www.helplib.com/ubuntu/article_170121) 
2. download link: [qt](http://download.qt.io/official_releases/qt/) 
3. path configuration
   1) 在命令端口中输入命令：sudo vim /usr/lib/x86_64-linux-gnu/qt-default/qtchooser/default.conf  打开default.conf文件。
   2) 将第一行改为自己安装路径（这是我的安装路径/home/wwf/software/Qt5.8.0）下的bin目录的路径，第二行改为Qt5.8.0目录的路径

   default is:
   ```path
    /usr/lib/x86_64-linux-gnu/qt4/bin
    /usr/lib/x86_64-linux-gnu           
    ```
    change to :
   ```path
   /home/sgl/Qt5.12.2/5.12.2/gcc_64/bin
   /home/sgl/Qt5.12.2/5.12.2
   ```
4. default desktop icon change, pls refer to the qt official website
5. [install qt ros package](https://blog.csdn.net/u010925447/article/details/81702166)

### 1.2.9. **PyQt5, python3 pycharm**
1. refer : https://www.jianshu.com/p/094928ac0b73

### 1.2.10. **Opencv**
1. download page, [opencv3.4.6](https://github.com/opencv/opencv/archive/3.4.6.zip)
2. install refer, [ubuntu16.04安装opencv3.4.1教程](https://blog.csdn.net/cocoaqin/article/details/78163171)

### 1.2.11. **pdf reader**
1. recommend Foxcit Reade; also **okular** is simple and useful,apt-get can be obtain.
2. download [Foxcit Reader](https://www.foxitsoftware.cn/downloads/), automatically choose the version for your computer system.
3. chmod of run file and sudo ./*.run if you want to install it for all files

### 1.2.12. **eric**
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

### 1.2.13. **java**
1. download page, [java jdk](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
2. install refer: [install jdk8](https://blog.csdn.net/u012707739/article/details/78489833), use last method

### 1.2.14. **arduino**
1. download page, [arduino](https://www.arduino.cc/en/main/software?setlang=cn)
2. install refer: [install arduino](https://linux.cn/article-6778-1.html)

### 1.2.15. **Vrep**
1. download page, [vrep](http://coppeliarobotics.com/ubuntuVersions.html)
2. install refer: [install vrep](https://www.cnblogs.com/21207-iHome/p/7855947.html)
3. [python vrep](https://github.com/Troxid/vrep-api-python)
