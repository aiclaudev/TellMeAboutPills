import cv2 

def img_Contrast(img): 
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8)) 
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR) 
    return final 

def img_gray(img) :
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def img_edge(img) :
    return cv2.Canny(img, 75, 75)

def img_denoise(img) :
    return cv2.fastNlMeansDenoising(img, h=40, templateWindowSize=7, searchWindowSize=21)  

def preprocessing(img) :
    img = img_Contrast(img)
    img = img_gray(img)
    img = img_edge(img)
    img = img_denoise(img)
    img = cv2.resize(img, dsize=(150, 150))
    return img


  