vins-mono 
---------
## TOOL
1. recent version of vins: [VINS-FUSION]( https://gitee.com/Luminary-S/VINS-Fusion/repository/archive/master.zip)
2. [Kalibr](https://github.com/ethz-asl/kalibr)
   
## hardware
现有的双目+6轴+（辅助： IR sensor）产品有， [高翔博士SLAM硬件体验：INDEMIND双目IMU相机](https://blog.csdn.net/weixin_43922139/article/details/97801193):
1. Stereo lab的ZED；双目相机，自身提供不错的功能比如深度估计和ZED Fusion；
2. DUO3d；红外双目相机，集成IMU；
3. 国内的perceptIn、小觅、远形、INDEMIND，等等。

## reference
1. [Kalibr标定Intel D435i相机](https://www.e-learn.cn/topic/2077891)
2. [RealSense T265相机及IMU标定，运行VINS](https://blog.csdn.net/Sunchanghaosch/article/details/103685866)
3. [用imu_utils标定IMU，之后用于kalibr中相机和IMU的联合标定](https://blog.csdn.net/fang794735225/article/details/92804030)
4. J. Maye, P. Furgale, R. Siegwart (2013). Self-supervised Calibration for Robotic Systems, In Proc. of the IEEE Intelligent Vehicles Symposium (IVS)
5. J. Kannala and S. Brandt (2006). A Generic Camera Model and Calibration Method for Conventional, Wide-Angle, and Fish-Eye Lenses, IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 28, no. 8, pp. 1335-1340
6. [解放双手——相机与IMU外参的在线标定](https://blog.csdn.net/electech6/article/details/95237412),相机与IMU的在线标定方法对比
7. [VINS-Mono代码分析总结](https://www.cnblogs.com/buxiaoyi/p/8660854.html)

## imu calibration

tools: [imu_utils](https://github.com/gaowenliang/imu_utils), [code_utils](https://github.com/gaowenliang/code_utils)

### problems
#### catkin_make imu and code utils, error occurs
solution:  compile code_utils first, then compile imu_utils;由于imu_utils 依赖 code_utils，所以先把code_utils放在工作空间的src下面，进行编译。然后再将imu_utils放到src下面，再编译
#### no "include <elfutils/libdw.h>" file error
solution: 
1. ```sudo apt-get install libdw-dev elfutils```
2. 在code_utils下面找到sumpixel_test.cpp，修改#include "backward.hpp"为 #include “code_utils/backward.hpp”

### Step
Note: 录制数据的时候一定要稍多于2小时，这样launch里面的120 才能得到完整的数据，否则减少120到配合你的录制数据时间
1. roslaunch sensor_startup imu_bringup.launch
2. rosbag record /imu_data -O imu.bag
3. rosbag play -r 200 imu.bag
4. source ~/catkin_new/devel/setup.bash 
5. 设置 imu_utils 的launch file, 设置 topic and save path
6. roslaunch imu_utils imu_ruifen.launch
* 经过这些标定会生成一个yaml文件和很多txt文件，主要是yaml文件，给出了加速度计和陀螺仪三轴的noise_density和random_walk，同时计算出了平均值，后面IMU+摄像头联合标定的时候需要这些均值。

## camera model calibration
[kalibr support model](https://github.com/ethz-asl/kalibr/wiki/supported-models)
   1. MEI model(Omnidirectional Camera, Unified projection model (C. Mei, and P. Rives, Single View Point Omnidirectional Camera Calibration from Planar Grids, ICRA 2007))
   2. pinhole model
### Step

   1. use Kalibr 生成 aprilgrid, refer to [calibration targets](https://github.com/ethz-asl/kalibr/wiki/calibration-targets)
   ```
   kalibr_create_target_pdf --type apriltag --nx 4 --ny 4 --tsize 0.048 --tspace 0.2
   ```
   2. publish highspeed camera topic (refer to usb-camera) ,直接ros publish 4hz rate
      ```
      roslaunch highspeed_cam highspeed_cam.launch
      ```
   1. 将标定目标AprilGrid置于相机前方合理距离范围内，然后缓慢移动标定目标，让所有摄像头均能看到标定物，移动目标1min左右即可。
   <!-- 2. 降低图像话题的频率，重新发布，kalibr在处理标定数据的时候要求图像的频率不可过高，一般为4hz，(多个就发布多次)：
      ```
      rosrun topic_tools throttle messages /highspeed_image_raw 4.0 /huagu_user1

      rosrun topic_tools throttle messages /camera/color/image_raw 4.0 /color
      rosrun topic_tools throttle messages /camera/infra2/image_rect_raw 4.0 /huagu_user1
      rosrun topic_tools throttle messages /camera/infra1/image_rect_raw 4.0 /huagu_user2
      ``` -->
   3. 然后进行录制：
      ```多个camera的录成一个bag 分别是两个topic,一个camera就只有一个topic
      rosbag record -O cam_cal /highspeed_image_raw 

      rosbag record -O multicameras_calibration /huagu_user1 /huagu_user2 /color
      rosbag play -r 2 <your bagfile> #可以看到运行的效果跟之前的不一样，这是因为回放是以 2 倍的速度去点击键盘的。
      ```
   4. 调用kalibr的算法计算各个摄像头的内参和外参
      ```
      kalibr_calibrate_cameras --target /home/sgl/catkin_new/src/highspeedCam/huagu/apriltags.yaml --bag /home/sgl/catkin_new/src/highspeedCam/huagu/cam_cal.bag --bag-from-to 26 100 --models pinhole-radtan --topics /highspeed_image_raw --show-extraction
      ```
      * apriltags.yaml -- 标定物的参数，具体是标定目标的尺寸之类，因为我是缩小打印在A4上，所以要对参数进行修改；                 pinhole-equi  -- 选择的相机模型，kalibr提供了很多相机模型，可以自己选择；
      ```april_6x6_A4.yaml 
         target_type: 'aprilgrid' #gridtype
         tagCols: 4               #number of apriltags
         tagRows: 4               #number of apriltags
         tagSize: 0.048           #size of apriltag, edge to edge [m]
         tagSpacing: 0.2          #ratio of space between tags to tagSize
                                 #example: tagSize=2m, spacing=0.5m --> tagSpacing=0.25[-]
      ```
      * --models : omni-radtan , pinhole-radtan 
      * --bag-from-to 可以选择时间段，毕竟录制的时候不能保证整体都录制的很好
### problem
1. [ERROR] [1542119711.427210]: [TargetViewTable]: Tried to add second view to a given cameraId & timestamp. Maybe try to reduce the approximate syncing tolerance.的问题，估计该问题是record得到的bag文件中camera的时间戳不一致导致，解决方法
   * 直接在 launch publish image的地方降采样为4hz，不要用throttle 重新publish 新的topic 

	Projection initialized to: [3386.88460723 3404.79638494  954.67112357  638.69118475]
	Distortion initialized to: [-0.5549834  -0.18364246 -0.00441096  0.00122816]
	Projection initialized to: [3439.20708416 3438.77924346  921.91485157  700.67494032]
	Distortion initialized to: [-0.59899896  0.30664106 -0.01652022  0.00272345]


## imu and camera TBC matrix calibration
   * tool: eth-asl/kalibr
  1. prepare calibration yaml file, refer to github wiki, [yaml formats](https://github.com/ethz-asl/kalibr/wiki/yaml-formats)
   * camchain.yaml (it's given by camera calibration)
   ``` 
   cam0:
  camera_model: pinhole
  intrinsics: [632.9640658678117, 638.2668942402212, 339.9807921782614, 243.68020465500277]
  distortion_model: equidistant
  distortion_coeffs: [0.366041713382057, 1.1433178097591097, -3.008125411486294, -3.1186836086733227]
  <!-- T_cam_imu:
  - [0.01779318, 0.99967549,-0.01822936, 0.07008565]
  - [-0.9998017, 0.01795239, 0.00860714,-0.01771023]
  - [0.00893160, 0.01807260, 0.99979678, 0.00399246]
  - [0.0, 0.0, 0.0, 1.0] -->
  #timeshift_cam_imu: -8.121e-05
  rostopic: /color
  resolution: [640, 480]
   ```
   * imu.yaml
   ```
   rostopic: /imu
   update_rate: 100.0 #Hz
   
   accelerometer_noise_density: 0.01 #continous
   accelerometer_random_walk: 0.0002 
   gyroscope_noise_density: 0.005 #continous
   gyroscope_random_walk: 4.0e-06
   ```
   2. [最好还是在roslaunch里面就改成相应的频率]将图像频率降低为20HZ，imu频率设置为200Hz,这里可以用throttle方法，不会出错，并发布新的topic，不会修改原topic：
```
rosrun topic_tools throttle messages /camera/color/image_raw 20.0 /color
rosrun topic_tools throttle messages /camera/gyro/image_info 200.0 /imu
```
   3. 录制rosbag包
```
rosbag record -O dynamic /color /imu
```
   4. 标定
```
kalibr_calibrate_imu_camera --target ./apriltags.yaml --cam ./camchain.yaml --imu ./imu.yaml --bag ./dynamic.bag --bag-from-to 5 25 --show-extraction
```

## vins-fusion 自定义设备运行

### step
1. 修改 config file 
2. 运行 vins_node 
   ```
    roslaunch vins vins_rviz.launch
    rosrun vins vins_node ~/catkin_new/src/VINS-Fusion/config/huagu/huagu_imu_config.yaml 
    (optional) rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_mono_imu_config.yaml 
    rosbag play YOUR_DATASET_FOLDER/MH_01_easy.bag  # if you run bag or launch your own devices
   ```

## vins-mono 运行

### Step
1. 修改 launch 文件
2. 运行vins_estimator and rviz
   ```
      roslaunch vins_estimator huagu.launch 
      roslaunch vins_estimator vins_rviz.launch
   ```


data: [0.99955035，  0.02812687，  0.01039147， -0.00076977，
         0.02213032， -0.92583519，  0.377279，0.0072113，
         0.02023247， -0.37687939， -0.92604134， -0.00292953，
         0，          0，          0，          1]