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