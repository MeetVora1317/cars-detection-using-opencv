import cv2

video = cv2.VideoCapture('video.avi')
carfile = cv2.CascadeClassifier('cars.xml')


while True:
    count,image= video.read()
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    cars = carfile.detectMultiScale(gray_image, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video2', image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
