NCS2 (Intel Neural compute stick 2)
----------

# Link
1. [OpenVINO install guide](https://docs.openvinotoolkit.org/latest/openvino_docs_install_guides_installing_openvino_linux.html) 
2. [干货|手把手教你在NCS2上部署yolov3-tiny检测模型](https://zhuanlan.zhihu.com/p/54984170)
3. [分享 | 英特尔第二代神经计算棒（Intel Neural Compute Stick 2）相关测试](https://blog.csdn.net/OpenVINOCC/article/details/108859934)


# model Optimizer
The Model Optimizer is a key component of the Intel Distribution of OpenVINO toolkit. You cannot perform inference on your trained model without running the model through the Model Optimizer. When you run a pre-trained model through the Model Optimizer, your output is an Intermediate Representation (IR) of the network. The Intermediate Representation is a pair of files that describe the whole model:

1.   .xml: Describes the network topology
2.   .bin: Contains the weights and biases binary data

# DL Workbench 

 DL Workbench is a platform built upon OpenVINO™ and provides a web-based graphical environment that enables you to optimize, fine-tune, analyze, visualize, and compare performance of deep learning models on various Intel® architecture configurations