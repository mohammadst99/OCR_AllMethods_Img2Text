
import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/Cellar/tesseract/5.1.0/bin/tesseract'
#/opt/homebrew/Cellar/tesseract/5.1.0/bin


def text(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(img))

def textbound(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(pytesseract.image_to_boxes(img))# give the word and x y w h

cap=cv.VideoCapture(0)




while True:
    sucess, img = cap.read()
    resizedIMG=cv.resize(img,(200 ,200))

    cv.imshow("Result", img)
    text(img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


