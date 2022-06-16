
# Detecting the Pills (In particular, White circular) based on YOLOv5
## Background and Need
* There are many people who take the pills incorrectly because they look similar. (In particular, old man) 
* The specialist pharmacist is responsible for re-classifying the pills returned by the patient (It is not right for medical professionals to engage in simple labor)

## The main content
* Based on the *YOLOv5* model, modeling AI that classifies 40 kinds of pills. 
* Among the 40 types of pills, the focus is on classifying 10 types of white circular pills.
  * This is because I saw a paper saying that white circular pills are not classified well because their properties are not noticeable.
* Because Project's second goal is Maximizing performance with limited datasets, Deliberately train a small number of data. (100 images per class) 
  * This is a hot issue in any area
* When using *YOLOv5* only, it shows less than 5% accuracy for the test set consisting of only white circular pills. 
* Therefore, after configuring an additional model, the detection performance is enhanced for white round pills by linking this model to YOLOv5.

## The goal of Model
* About 70% accuracy for white circular pills. (This is not high, but original YOLOv5's accuarcy is less than 5%) 
* One of the strength of YOLOv5 is fast inference speed. So Maintaining inference speed is my second goal.


## Entire Model
<img src="https://user-images.githubusercontent.com/88221233/174103787-234484df-b436-4f1e-b5ae-e6afa7e19d40.jpg"  width="600" height="400"/>

* Other pills(not white circular) are predicted only using YOLOv5. 
* But when some pills are identified white circular, YOLOv5 delivers the bounding box value to new model.
* The image surrounded by bounding box is finally classified with new model.
* New model delivers the class label to YOLOv5, and YOLOv5 updates a class label for some objects.

## New model structure
<img src="https://user-images.githubusercontent.com/88221233/174103632-49e63dd3-f8ad-49ec-bdc3-af07b2a54cea.png"  width="400" height="500"/>



## How to do it?
1. You can get images about pills in [here](https://nedrug.mfds.go.kr/pbp/CCBGA01/getItem?infoName=%EB%82%B1%EC%95%8C&totalPages=6&limit=10&searchYn=true&page=1&&openDataInfoSeq=11)
2. Construct the dataset using [labelImg](https://github.com/tzutalin/labelImg), [Imgaug](https://github.com/aleju/imgaug) <img src="https://user-images.githubusercontent.com/88221233/174101720-371efe94-c050-44a5-ac0a-5d8f991ba520.png"  width="800" height="400"/>
3. Train the original YOLOv5 using above data set
4. Train the my custom model using above data set(**But only using white circular pills**)
5. Connect YOLOv5 and new model

## Result
Original YOLOv5            |  My YOLOv5
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/88221233/174106647-8c3470b3-9db7-41ac-82e3-c076ad357dc6.jpg)  |  ![](https://user-images.githubusercontent.com/88221233/174106924-73eed80f-4411-4aca-b5be-04d3389fe66e.jpg)

* Accuracy is less than 5% when using original YOLOv5.
* Accuarcy is about 60% when using my YOLOv5 that connect with new model.
* Because accuarcy is not high, I can not say that My YOLOv5 is so great 
* But, I can say that there is a definite performance improvement compared to the original YOLOv5.
* And, there is no inference speed decline.
* I think we can improve performance if we learn more data. (But, I used 100 images per class)

## Reference
> 이경윤, 김영재, 김승태, 김효은, 김광기 (2019). 알약 자동 인식을 위한 딥러닝 모델간 비교 및 검증. 멀티미디어학회 논문지, 22(3), 349-356

> 강성민. “딥러닝을 이용한 자동 알약 인식.”국내석사학위논문 성균관대학교 일반대학원, 2021. 서울

> 배소현, 손수현, 전예진, 황선정 (2020). 스마트폰으로 촬영된 알약 이미지의 식별 마크 인식 모델을 이용한 알약 인식 및 정보 제공 시스템. 한국정보과학회 학술발표논문집, 1361-1363.

> https://nedrug.mfds.go.kr/pbp/CCBGA01/getItem?infoName=%EB%82%B1%EC%95%8C&totalPages=6&limit=10&searchYn=true&page=1&&openDataInfoSeq=11

> https://github.com/ultralytics/yolov5

> https://gist.github.com/fchollet

> https://ropiens.tistory.com/44
