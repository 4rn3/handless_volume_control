import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("data gathering")
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("thumb", frame)

    key = cv2.waitKey(1)

    if key == ord('u'):
        img_name = "thumb_up_{}.png".format(img_counter)
        cv2.imwrite("./raw_up/"+img_name, frame)
        img_counter += 1
    
    if key == ord('d'):
        img_name = "thumb_down_{}.png".format(img_counter)
        cv2.imwrite("./raw_down/"+img_name, frame)
        img_counter += 1

    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
