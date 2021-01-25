ROS系统平时工作中使用的命令工具
----

#### 查看ROS_PACKAGE_PATH环境变量
```
echo $ROS_PACKAGE_PATH
/home/saneri/catkin_ws/src:/opt/ros/kinetic/share
```
#### 创建一个package
```
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```
#### roscore  命令是
在运行所有ROS程序前首先要运行的命令。


#### rosrun 命令
rosrun 允许你使用包名直接运行一个包内的节点(而不需要知道这个包的路径)。

用法:
rosrun [package_name] [node_name]

现在我们可以运行turtlesim包中的 turtlesim_node节点,你会看到打开了一个 turtlesim 窗口:
```
rosrun turtlesim turtlesim_node
```
#### rosls 命令
rosls是rosbash命令集中的一部分，它允许你直接按软件包的名称而不是绝对路径执行ls命令(罗列目录).

用法：
rosls  [ 本地包名称[/子目录] ]

```
rosls beginner_tutorials/
CMakeLists.txt  include  package.xml  src
``` 

#### roscd 命令
roscd是rosbash命令集中的一部分，它允许你直接切换(cd)工作目录到某个软件包或者软件包集当中。
用法：
roscd [ 本地包名称[/子目录] ]

```
roscd roscpp
pwd
/opt/ros/kinetic/share/roscpp
```

#### roscd log命令
使用roscd log可以切换到ROS保存日记文件的目录下。需要注意的是，如果你没有执行过任何ROS程序，系统会报错说该目录不存在。

如果你已经运行过ROS程序，那么可以尝试：
```
roscd log
```

#### rosnode 命令
rosnode 显示当前运行的ROS节点信息
```
rosnode list                  获得运行节点列表
rosnode info node-name        获得特定节点的信息
rosnode ping  node-name       测试节点是否连通
rosnode kill node-name        终止节点
```

#### rosed 命令
rosed 是 rosbash 的一部分。利用它可以直接通过package名来获取到待编辑的文件而无需指定该文件的存储路径了。
使用方法
$ rosed [package_name] [filename]
例子:
```rosed roscpp Logger.msg```
这个实例展示了如何编辑roscpp package里的Logger.msg文件。

#### rospack 命令
rospack允许你获取软件包的有关信息

用法：
rospack find [包名称]
实例：
要找到一个软件包的目录，使用 rospack find命令
```
rospack find roscpp
/opt/ros/kinetic/share/roscpp

rospack list 　　　　　　　　　　　　　　   #显示出当前的包信息
rospack depends1 beginner_tutorials  　　    #显示当前包的一级依赖
rospack depends beginner_tutorials 　　　　#显示当前包的所有依赖
``` 

#### rostopic 命令
rostopic命令工具能让你获取有关ROS话题的信息。
你可以使用帮助选项查看rostopic的子命令：
```
$ rostopic -h
Commands:
        rostopic bw     display bandwidth used by topic(显示主题使用的带宽)
        rostopic delay  display delay of topic from timestamp in header(从标题中的时间戳显示主题的延迟)
        rostopic echo   print messages to screen(将消息打印到屏幕)
        rostopic find   find topics by type(按类型查找主题)
        rostopic hz     display publishing rate of topic(显示主题的发布率)  
        rostopic info   print information about active topic(打印有关活动主题的信息)
        rostopic list   list active topics(列出活动主题)
        rostopic pub    publish data to topic(将数据发布到主题)
        rostopic type   print topic or field type(打印主题或字段类型)
```

1. 使用 rostopic list
rostopic list能够列出所有当前订阅和发布的话题,让我们查看一下list子命令需要的参数.
```
$ rostopic list -h
Usage: rostopic list [/namespace]

Options:
  -h, --help            show this help message and exit(显示此帮助消息并退出)
  -b BAGFILE, --bag=BAGFILE
                        list topics in .bag file(列出.bag文件中的主题)
  -v, --verbose         list full details about each topic(列出每个主题的完整详细信息)
  -p                    list only publishers(仅列出发布商)
  -s                    list only subscribers(仅列出订阅者)
  --host                group by host name(按主机名分组)
```
2. 在rostopic list 中使用 verbose 选项,这会显示出有关所发布和订阅的话题及其类型的详细信息。

```
$ rostopic list -v

Published topics:
 * /turtle1/color_sensor [turtlesim/Color] 1 publisher
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 publisher
 * /rosout [rosgraph_msgs/Log] 3 publishers
 * /rosout_agg [rosgraph_msgs/Log] 1 publisher
 * /turtle1/pose [turtlesim/Pose] 1 publisher

Subscribed topics:
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 subscriber
 * /rosout [rosgraph_msgs/Log] 1 subscriber
 * /statistics [rosgraph_msgs/TopicStatistics] 1 subscriber
 ```

* 仅列出发布者
    ```
    $ rostopic list -p
    /rosout
    /rosout_agg
    /turtle1/cmd_vel
    /turtle1/color_sensor
    /turtle1/pose
    ```
  * 仅列出订阅者
    ```
    $ rostopic list -s
    /rosout
    /statistics
    /turtle1/cmd_vel
    ```
3. rostopic echo 可以显 示在某个话题上发布的数据.
```
rostopic echo /rosout_agg
```
4. rostopic type 命令用来查看所发布话题的消息类型。
```
$ rostopic type /turtle1/color_sensor
turtlesim/Color
$ rostopic type /turtle1/cmd_vel
geometry_msgs/Twist
```

5. 使用 rostopic pub
rostopic pub可以把数据发布到当前某个正在广播的话题上。
用法：

$ rostopic pub [topic] [msg_type] [args]

```
rostopic list                    #查出所有rostopic
/rosout
/rosout_agg
/statistics
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

saneri@localhost:~$ rostopic type /turtle1/cmd_vel        #查类型
geometry_msgs/Twist

$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```

以上命令会发送一条消息给turtlesim，告诉它以2.0大小的线速度和1.8大小的角速度开始移动。
```
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```
这条命令以1Hz的频率发布速度命令到速度话题上。

6. 使用 rostopic hz
rostopic hz命令可以用来查看数据发布的频率。
用法：
```
rostopic hz [topic]
rostopic hz /turtle1/pose

result:
subscribed to [/turtle1/pose]
average rate: 62.486
        min: 0.015s max: 0.017s std dev: 0.00047s window: 60
average rate: 62.476
        min: 0.015s max: 0.018s std dev: 0.00045s window: 122
average rate: 62.514
        min: 0.014s max: 0.020s std dev: 0.00057s window: 185
average rate: 62.506
        min: 0.013s max: 0.020s std dev: 0.00061s window: 248
```
7. rostopic type和rosmsg show命令来获取关于某个话题的更深层次的信息。
```
$ rostopic type /turtle1/cmd_vel | rosmsg show
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```

#### rosmsg命令
来查看消息的详细情况。
```
$ rosmsg show geometry_msgs/Twist
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```

#### rosbag 命令
rosbag 将ROS系统运行过程中的数据录制到一个.bag文件中，然后可以通过回放数据来重现相似的运行过程.退出录制时按Ctrl-C退出该命令，你应该会看到在当前目录下一个以年份、日期和时间命名并以.bag作为后缀的文件。

录制所有发布的话题,其中 -a 选项，该选项表示将当前发布的所有话题数据都录制保存到一个bag文件中。
```
rosbag record -a
```
回放bag文件以再现系统运行过程
```
$ rosbag play <your bagfile>

# 以某一频率发布消息(控制bag包播放的频率) : 
   rosbag play -r 2

# 从某一时间节点开始播放发布消息 
 rosbag play -s 2

# 查看bag文件信息
 rosbag info <your bagfile>

录制数据子集
rosbag record命令支持只录制某些特别指定的话题到单个bag文件中，这样就允许用户只录制他们感兴趣的话题

#在bag文件所在目录下执行以下命令,-O参数告诉rosbag record将数据记录保存到名为2018-12.bag 的文件中，同时后面的话题参数告诉rosbag record只能录制这两个指定的话题。
rosbag record -O 2018-12.bag  /turtle1/command_velocity /turtle1/pose


#查看录制时指定话题的信息.
rosbag info 2018-12.bag

#也可以只指定bag包的文件名，录制所有数据
rosbag record -a -O 2018-12.bag

#录取指定topic，并且每五分钟分割一次, -e为正则匹配。
rosbag record --split --duration=5m -e /radar/back_targets /vehicle_speed /imu_data
```

如果查看视频，可以执行如下命令，就可以实现视频播放功能
```
rosrun image_view image_view image:=/camera/front_middle compressed
```
