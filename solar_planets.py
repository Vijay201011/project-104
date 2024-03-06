import cv2
img=cv2.imread('solar-system.jpg')

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (100,100,100),
            )

cv2.putText(img,
            "Mercury",
            (100,250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (200,200,0),
            )

cv2.putText(img,
            "Venus",
            (180,250),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255,0,255),
            )

cv2.putText(img,
            "Earth",
            (250,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "Mars",
            (350,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "Jupiter",
            (420,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "Saturn",
            (700,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "Uranus",
            (900,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "Neptune",
            (1111,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )
cv2.imshow('output',img)
cv2.waitKey(0)


