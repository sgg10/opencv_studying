import cv2

image = cv2.imread("logo_platzi.png")
# cv2.imwrite("logo_platzi2.png", image)
cv2.imshow("Logo de la razon de media vida nuestra", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

