# Detecting low contrast images with OpenCV, scikit-image, and Python

 you are able to control the environment and, most importantly, *the lighting* when you capture an image, the easier it will be to write code to process the image.

With controlled lighting conditions you’re able to hard-code parameters, including:

- Amount of blurring
- Edge detection bounds
- Thresholding limits
- Etc.

## **What problems do low contrast images/frames create? And how can we detect them?**

<img src = "https://user-images.githubusercontent.com/59350891/112761683-5777c480-9037-11eb-936c-33c39a44530c.png" width=60%>

- 왼쪽은 카드의 윤곽선을 감지하기 어려운 저 대비 이미지의 예
- 오른 쪽은 카드 감지가 훨씬 쉬운 고 대비 이미지

## **Configuring your development environment**

`pip install opencv-contrib-python`

`pip install scikit-image`

## Implementing low contrast image detection with OpenCV

### Canny Edge

- 이제까지 논의된 엣지 검출기들보다 우월한 알고리즘
- 윤곽을 잘 찾아내면서도 원래 영상의 회색물질과 관련된 모든 엣지들을 제거할 수 있는 유일한 방법
- 그러나 구현이 복잡하고 실행 시간이 길다







