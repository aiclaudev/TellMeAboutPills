
# Detecting the Pills (In particular, White circular) based on YOLOv5
## Background and Need
* There are many people who take the pills incorrectly because they look similar. (In particular, old man) 
* The specialist pharmacist is responsible for re-classifying the pills returned by the patient (It is not right for medical professionals to engage in simple labor)

## The main content
* Based on the *YOLOv5* model, modeling AI that classifies 40 kinds of pills. 
* Among the 40 types of pills, the focus is on classifying 10 types of white circular pills. 
* Because Project's second goal is Maximizing performance with limited datasets, Deliberately train a small number of data. (100 images per class) 
* When using *YOLOv5* only, it shows less than 5% accuracy for the test set consisting of only white circular pills. 
* Therefore, after configuring an additional model, the detection performance is enhanced for white round pills by linking this model to YOLOv5.

## The goal of Model
* About 70% accuracy for white circular pills. (This is not high, but original YOLOv5's accuarcy is less than 5%) 
* One of the strength of YOLOv5 is fast inference speed. So Maintaining inference speed is my second goal.

## 
