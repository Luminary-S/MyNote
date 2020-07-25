[Underactuated Robotics](http://underactuated.mit.edu/index.html)
course from MIT,  Russ Tedrake
git: https://github.com/RussTedrake/underactuated
-------

# ASIMO((Advanced Step in Innovative MObility))
1. **late 1996**, Honda Motor Co.
2.  Although the motions are very smooth, there is something <font color=#FF0000>a little unnatural about ASIMO's gait</font>. It feels a little like an astronaut encumbered by a heavy space suit.
3.  ASIMO is walking a bit like <font color=#FF0000>somebody that is unfamiliar with his/her dynamics</font>. Its control system is <font color=#FF0000>using high-gain feedback, and therefore considerable joint torque</font>, to cancel out the natural dynamics of the machine and strictly follow a desired trajectory.
4.   This control approach comes with a stiff penalty. ASIMO <font color=#FF0000>uses roughly 20 times the energy (scaled) that a human uses</font> to walk on the flat (measured by cost of transport)[1].
5.    Also, control <font color=#FF0000>stabilization in this approach only works in a relatively small portion of the state space</font> (when the stance foot is flat on the ground), so ASIMO <font color=#2dd4b8>can't move nearly as quickly as a human, and cannot walk on unmodelled or uneven terrain</font>. 

# passive dynamic walker (PDW)
1. [A 3D passive dynamic walker by Steve Collins and Andy Ruina--Cornell](http://groups.csail.mit.edu/locomotion/elib.cgi?b=Collins01)
2. no motors, no controllers, no computer, but is still capable of walking stably down a small ramp, <font color=#FF0000>powered only by gravity</font>
3. Passive walkers demonstrate that the high-gain, dynamics-cancelling feedback approach taken on ASIMO is not a necessary one. In fact, <font color=#FF0000>the dynamics of walking is beautiful, and should be exploited - not cancelled out</font>

# Boston Dynamics
Boston Dynamics' Atlas robot does a backflip， a marvel of engineering

# Manipulation

## stereotypical pipeline
1.  we enumerate a handful of contact locations on the hand (these points, and only these points, are allowed to contact the world). 
2.  given a localized object in the environment, we plan a collision-free trajectory for the arm that will move the hand into a "pre-grasp" location. 
3.  At this point the robot closes it's eyes (figuratively) and closes the hand, hoping that the pre-grasp location was good enough that the object will be successfully grasped using e.g. only current feedback in the fingers to know when to stop closing. 
4.  "Underactuated hands" make this approach more successful, but the entire approach really only works well for enveloping grasps. 

## human manipulation
1. the contact interactions with the object and the world are very rich -- we often use pieces of the environment as fixtures to reduce uncertainty,
2. we commonly exploit slipping behaviors (e.g. for picking things up, or reorienting it in the hand)
3. our brains don't throw NaNs if we use the entire surface of our arms to e.g. manipulate a large object. 
4. efficiency, agility, and robustness

# Feedback Equivalence
<!-- <img src="/home/sgl/MyNote/underactuated_robotics/img/underactuated_sys_eq.png"  style="zoom: 25%;" /> -->
![underactuated system equation](/home/sgl/MyNote/underactuated_robotics/img/underactuated_sys_eq.png)
Fully-actuated systems are dramatically easier to control than underactuated systems. 
 The key observation is that, for fully-actuated systems with known dynamics , it is possible to use feedback to effectively change an arbitrary control problem into the problem of controlling a trivial linear system. 