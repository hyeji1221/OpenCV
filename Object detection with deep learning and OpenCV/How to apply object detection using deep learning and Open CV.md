## How to apply object detection using deep learning and Open CV

**ObjectDetection 이란?**

- 컴퓨터 비전 중, 카메라를 통해 얻을 수 있는 이미지 스트림에서 물체를 인식하는 기술 

using Single Shot Detector and Mobile Net  -> can be used for super fast, real-time object detection on resource constrained devices (including the Raspberry Pi, smartphones, etc.)

딥러닝을 통한 객체 탐지 모델은 크게 **R-CNN, SSD, YOLO**

#### R-CNN

- 가장 전통적인 방법이지만 이해하고 구현하기 어려움 & 속도 느림

#### YOLO

- R-CNN보다 속도 빠르지만 정확도가 좋지 않음

#### SSD

- 구글에서 개발
- R-CNN과 YOLO의 중간 (R-CNN보다 구현하기 쉬움, YOLO보다 정확함)

#### MobileNets : Efficient (deep) neural networks

- they are designed for resource constrained devices such as your smartphone
- MobileNets differ from traditional CNNs through the usage of *depthwise separable convolution* -> The problem is that we sacrifice accuracy and MobileNets are normally not as accurate but 자원은 효율적임
-  general idea behind depthwise separable convolution is to split convolution into two stages:
  - A *3×3* depthwise convolution.
  - Followed by a *1×1* pointwise convolution.

<img src = "https://user-images.githubusercontent.com/59350891/111908222-c5524800-8a9b-11eb-9de8-c2f325d8cf51.png" width = 45%>

왼쪽 그림은 일반적인 convolution에서 사용하는 방법 오른쪽 그림이 mobilenet에서 사용하는 방법

-> 기존의 convolution 연산을 depthwise seperable convolution으로 쪼개 필요한 연산을 줄임 

(output 채널 개수와 커널 사이즈 관계를 depwise Conv와 1x1 conv로 쪼개서 연산량을 줄임)

[컨볼루션 설명](https://eehoeskrap.tistory.com/431)

<img src = "https://user-images.githubusercontent.com/59350891/111909543-0f89f800-8aa1-11eb-8ea5-bc49fcd8f378.png" width = 75%>

### Combining MobileNets and Single Shot Detectors(SSD) for fast, efficient deep-learning based object detection

https://github.com/chuanqi305/MobileNet-SSD -> 사용할 모델

We can therefore detect 20 objects in images (+1 for the background class), including *airplanes, bicycles, birds, boats, bottles, buses, cars, cats, chairs, cows, dining tables, dogs, horses, motorbikes, people, potted plants, sheep, sofas, trains,* and *tv monitors*.





