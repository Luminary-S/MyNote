强化学习原理：如果智能体对某些动作进行奖励，之后执行该动作的概率就会增加；反之，若惩罚，执行概率就会降低。
强化学习分类：
基于价值的强化学习：分析所处环境，输出下一步行动的概率分布，根据概率分布采取行动。
基于策略的强化学习：输出每种行动的价值，一般是基于最高价值来选择行动。
将二者结合，就是actor-critic算法：演员基于策略作出相关动作，而评论家利用价值函数，给出行动的价值分数，即在原有策略梯度的方法上，加速了策略学习的过程。
深度学习：对输入数据进行特征学习，并且通过分层次的多层网络得到特征信息，从而使机器理解学习数据，获得特征信息。
深度强化学习：深度学习用于提取数据，强化学习用于决策，二者结合可以给解决复杂系统的感知决策问题提供有效方法。
DDPG算法：采用actor-critic框架，由4个神经网络组成，2个结相同的网络，分别是actor网络和critic网络。actor选出动作网络，输入状态，输出状态。critic网络评价动作网络，输入状态，输出Q值（机器人手臂的动作值）。对目标值与Q值的差，和其导数，作为误差，误差小则获得奖励多。
————————————————
版权声明：本文为CSDN博主「MIJIAMAN」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_43123223/article/details/90648876