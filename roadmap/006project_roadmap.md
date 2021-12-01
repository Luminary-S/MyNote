The window cleaning robot can be divided into three aspects requirements:
1. system performance
2. demonstration completion
3. theoretical creation

**_Roadmap 1_**
system feasible -> theoretical creation -> system performance ->demonstration completion ->theoretical creation -> system performance -> theoretical breakthrough

Roadmap 1 is the nowadays routine of my project, but it leads to the slowly development of the theoretical output, mainly due to the over-reliance on the hardware performance, and the hardware are updated day by day.

**_Roadmap2_**
system feasible -> theoretical creation -> key part performance ->demonstration completion ->theoretical upgrade -> key part performance -> theoretical breakthrough

force_torque_sensor_calib
------

## pre-requisite
1. F/T measurement
2. gravity measurements of the accelerometer gravity is assumed to be expressed in the F/T sensor frame

## revise
`ft_calib_node.cpp`

### FTCalibNode()
1. topic name revise: "ft_raw"->"ft_sensor"

### getROSParameters()
1. yaml file set : "moveit_group_name", "calib_file_name", "calib_file_dir", "meas_file_name", "meas_file_dir", "poses_frame_id", "random_poses", "number_random_poses"
2. pose in [x y z r p y] format ([m], [rad])

## result
Least squares to estimate the F/T sensor parameters
The estimated parameters are : [m m*cx m*cy m*cz FBx FBy FBz TBx TBy TBz]
1.  m: mass of the gripper
2. [cx, cy, cz] are the coordinates of the center of mass of the gripper
3. FB : force bias
4. TB: torque bias
5. All expressed in the FT sensor frame