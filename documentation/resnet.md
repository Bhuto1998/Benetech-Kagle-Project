# ResNet

### **ResNet (Residual Networks)**

ResNet, short for Residual Networks, is a popular convolutional neural network (CNN) architecture widely used in the field of computer vision.

#### **1. History and Motivation**

ResNet was introduced by Kaiming He et al., from Microsoft Research, in the paper titled "Deep Residual Learning for Image Recognition" at the CVPR conference in 2015. This network addressed a fundamental problem in deep learning: the degradation problem. As neural networks become deeper, they should be able to perform better. However, due to problems such as vanishing and exploding gradients, the performance would saturate and then degrade rapidly. The authors proposed ResNet to alleviate this issue.

#### **2. Architecture**

The main innovation of ResNet is the introduction of the "residual block" or "skip connection" concept. Instead of trying to learn an underlying mapping directly, they aimed to learn the residual representation. Mathematically, if H(x) is the desired underlying mapping, instead of trying to learn H(x), they try to learn F(x) = H(x) - x, which they call the residual. Therefore, the original function becomes H(x) = F(x) + x.

In the standard feedforward neural network, each layer feeds into the next layer. In a network with residual blocks, each layer feeds into the next layer and directly into the layers about 2-3 hops away. That's why they're called "skip connections", as the input to a layer is used as part of the output of a later layer in the network.

**2.1 Residual Block**

The core component of a ResNet is the residual block. A basic residual block consists of several convolutional layers and a "shortcut" or "skip connection" that bypasses these layers.

A standard ResNet block consists of:

* A Convolution Layer
* A Batch Normalization Layer
* A ReLU Activation Layer
* Another Convolution Layer
* Another Batch Normalization Layer
* Addition with the Shortcut
* A ReLU Activation Layer

The exact number and size of the convolutional layers can vary, and more complex variants of the residual block use bottleneck structures with 1x1 convolutions.

#### **3. Variants of ResNet**

The original ResNet paper proposed ResNet models with different depths, including ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152. The number refers to the number of layers in the network.

Later, other variants of ResNet were proposed by the community, including ResNet-200, ResNeXt, and Wide ResNet. These variants try to increase the accuracy by making the network deeper or wider, or by changing the structure of the residual blocks.

#### **4. Applications**

ResNets have been successfully used in a variety of computer vision tasks, including image classification, object detection, and semantic segmentation. They have been particularly successful in large-scale image recognition tasks and have achieved state-of-the-art performance in ImageNet classification, COCO object detection, and other benchmarks.

#### **5. Advantages and Disadvantages**

**Advantages:**

* ResNet alleviates the vanishing/exploding gradient problem and enables the training of very deep neural networks.
* ResNet has achieved excellent performance in various tasks and is often used as a backbone network in many computer vision tasks.
* Skip connections help to preserve the gradient flow in the network, making it easier to train.

**Disadvantages:**

* While ResNets can be very deep, they are also quite large, which can make them slower to train

and use more memory.

* The design of ResNet is more complex than a standard CNN due to the addition of skip connections.

***
