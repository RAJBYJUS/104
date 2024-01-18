import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(100,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
    

cv2.putText(img,"Mercury", (110,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))


cv2.putText(img,"Venus", (180,220),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))


cv2.putText(img,"Earth", (280,220),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))


cv2.putText(img,"Mars", (380,220),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Jupiter", (480,220),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
)

cv2.putText(img,"Saturn", (680,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Uranus", (890,125),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune", (1000,125),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("Output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)